#!/bin/bash
set -e

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh

echo ""
echo "Sleeping for ${UE1_STARTUP_DELAY} seconds to allow the 5G core and GNB to start"
echo ""
sleep ${UE1_STARTUP_DELAY}

if [ -f ${RESULTS_FOLDER}/roughData/UE1_metrics.jsons ]; then
    sudo rm -f ${RESULTS_FOLDER}/roughData/UE1_metrics.json
fi

# start the UE1
sudo srsue /etc/srsran/ue1.conf