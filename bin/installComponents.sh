#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh

# ensure we are ready to run the 5G core
sudo ./deploy-srs.sh release_24_04 srsRAN_Project

# ensure we are ready to run the 4G gNodeB
sudo ./deploy-srs.sh release_23_11 srsRAN_4G


# install other components
sudo apt install -y python3-pip
sudo pip install ruamel.yaml jsonstream matplotlib


# create a network namespace for the UE(s)
for i in {1..4}
do
    sudo ip netns add ue${i} || true
done

#############################################
# Create the results folder
sudo mkdir -p ${RESULTS_FOLDER}
sudo chmod a+rwx ${RESULTS_FOLDER}
sudo mkdir -p ${RESULTS_FOLDER}/data/
sudo chmod a+rwx ${RESULTS_FOLDER}/data/
sudo mkdir -p ${RESULTS_FOLDER}/roughData/
sudo chmod a+rwx ${RESULTS_FOLDER}/roughData/



##############################################################
# setup the good gNodeB config file

# copy the existing gnb conf file to a new one
sudo cp /etc/srsran/gnb.conf /etc/srsran/gnb_good.conf

# Modify the good config file to report statistics
sudo ${SCRIPT_DIR}/modifyGnbConfig.py -f /etc/srsran/gnb_good.conf --metricsIpAddr 127.0.0.1 --metricsPort 55555


##############################################################
# setup the EVIL gNodeB config file

# copy the existing gnb conf file to a new one
sudo cp /etc/srsran/gnb.conf /etc/srsran/gnb_evil.conf

# Modify the good config file to report statistics
sudo ${SCRIPT_DIR}/modifyGnbConfig.py -f /etc/srsran/gnb_evil.conf --metricsIpAddr 127.0.0.1 --metricsPort 55556 --testMode


##############################################################
# setup the UE(s)'s' config file
echo "Writing modified UE files to /etc/srsran/   (turning on json logging)"
for i in {1..4}
do
    cp /etc/srsran/ue.conf /tmp/ue${i}.conf
    echo "[general]"                                                               >> /tmp/ue${i}.conf
    echo "metrics_json_enable   = true"                                            >> /tmp/ue${i}.conf
    echo "metrics_json_filename = ${RESULTS_FOLDER}/roughData/UE${i}_metrics.json" >> /tmp/ue${i}.conf
    sudo cp /tmp/ue${i}.conf /etc/srsran/
done



