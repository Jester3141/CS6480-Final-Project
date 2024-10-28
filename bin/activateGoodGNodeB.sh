#!/bin/bash
set -e

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh


# ensure we are ready to run the 4G gNodeB
CheckFor4gGNBSetup



echo ""
echo "Sleeping for ${GOOD_GNODEB_STARTUP_DELAY} seconds to allow the 5G core to start"
echo ""
sleep ${GOOD_GNODEB_STARTUP_DELAY}

# start the Evil gNodeB
sudo gnb -c /etc/srsran/gnb_good.conf
