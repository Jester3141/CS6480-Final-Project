#!/bin/bash
set -e

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh

echo ""
echo "Sleeping for ${UE1_IPERF_CLIENT_STARTUP_DELAY} seconds to allow the 5G core and GNB to start"
echo ""
sleep ${UE1_IPERF_CLIENT_STARTUP_DELAY}

sudo mkdir -p ${RESULTS_FOLDER}
sudo chmod a+rwx ${RESULTS_FOLDER}

if [ -f ${RESULTS_FOLDER}/roughData/UE1_iperf_results.jsons ]; then
    sudo rm -f ${RESULTS_FOLDER}/roughData/UE1_iperf_results.json
fi


# start iperf3 client for UE1 and pass traffic on the downlink
echo "Starting IPerf3 Client.  Output is being redirected to file so you won't see anything. This is normal."
sudo ip netns exec ue1 iperf3 -c 10.45.1.1 -R --json --logfile ${RESULTS_FOLDER}/roughData/UE1_iperf_results.json