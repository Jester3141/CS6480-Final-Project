#!/bin/bash
set -e

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh
source /local/generated/timings.sh

echo "Starting IPerf3 Server"
# ensure that we have clean state
set +e
sudo killall -q iperf3
set -e




# start iperf3 server
sudo iperf3 -s -p 5201 &
sudo iperf3 -s -p 5202 &
sudo iperf3 -s -p 5203 & 
sudo iperf3 -s -p 5204 &