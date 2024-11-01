#!/bin/bash
set -e

UE_STARTUP_DELAY=0

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh

echo ""
echo "Sleeping for ${UE_STARTUP_DELAY} seconds to allow the 5G core and GNB to start"
echo ""
sleep ${UE_STARTUP_DELAY}

if [ -f ${RESULTS_FOLDER}/roughData/UE_metrics.jsons ]; then
    sudo rm -f ${RESULTS_FOLDER}/roughData/UE_metrics.json
fi


# turn on the modem
sudo sh -c "chat -t 1 -sv '' AT OK 'AT+CFUN=1' OK < /dev/ttyUSB2 > /dev/ttyUSB2"


# launch the the quectel UE app
sudo quectel-CM -s internet -4

