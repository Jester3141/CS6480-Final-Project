#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh


# install other components
sudo apt install -y python3-pip
sudo pip install ruamel.yaml jsonstream matplotlib



#############################################
# Create the results folder
sudo mkdir -p ${RESULTS_FOLDER}
sudo chmod a+rwx ${RESULTS_FOLDER}
sudo mkdir -p ${RESULTS_FOLDER}/data/
sudo chmod a+rwx ${RESULTS_FOLDER}/data/
sudo mkdir -p ${RESULTS_FOLDER}/roughData/
sudo chmod a+rwx ${RESULTS_FOLDER}/roughData/


#TODO

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

