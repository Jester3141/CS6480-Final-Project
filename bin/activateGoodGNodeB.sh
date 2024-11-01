#!/bin/bash
set -e

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh
source /local/generated/timings.sh

echo ""
echo "Sleeping for ${GOOD_GNODEB_STARTUP_DELAY} seconds to allow the 5G core to start"
echo ""
sleep ${GOOD_GNODEB_STARTUP_DELAY}

echo ""
echo "Starting good gNodeB"
echo ""





sudo /var/tmp/srsRAN_Project/build/apps/gnb/gnb -c /var/tmp/etc/srsran/gnb_rf_x310_tdd_n78_40mhz.yml -c /local/generated/goodGNodeBConfig.yaml

