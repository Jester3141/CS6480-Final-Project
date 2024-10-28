#!/bin/bash
set -e

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh

# ensure that we have clean state
set +e
sudo killall -q iperf3
set -e




# start iperf3 server
sudo iperf3 -s