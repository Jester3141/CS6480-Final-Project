#!/bin/bash
set -e

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh

# ensure that we have clean state
set +e
sudo killall -q iperf3
set -e

echo ""
echo "Sleeping for ${IPERF3_STARTUP_DELAY} seconds to allow the 5G core and GNB to start"
echo ""
sleep ${IPERF3_STARTUP_DELAY}



# start iperf3 server within the 5gc docker container
sudo docker exec -it open5gs_5gc iperf3 -s