#!/bin/bash
set -e

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh


# ensure we are ready to run the 4G gNodeB
#CheckFor4gGNBSetup

# copy the existing gnb conf file to a new one
sudo cp /var/tmp/etc/srsran/gnb_rf_x310_tdd_n78_40mhz.yml /var/tmp/etc/srsran/gnb_rf_x310_tdd_n78_40mhz_good.yml

# Modify the good config file to report statistics
sudo ${SCRIPT_DIR}/modifyGnbConfig.py -f /var/tmp/etc/srsran/gnb_rf_x310_tdd_n78_40mhz_good.yml --metricsIpAddr 127.0.0.1 --metricsPort 55555


sudo /var/tmp/srsRAN_Project/build/apps/gnb/gnb -c /var/tmp/etc/srsran/gnb_rf_x310_tdd_n78_40mhz_good.yml

