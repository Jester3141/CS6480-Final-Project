#!/bin/bash
set -e

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh

echo ""
echo "Sleeping for ${UE1_PING_STARTUP_DELAY} seconds to allow the 5G core and GNB to start"
echo ""
sleep ${UE1_PING_STARTUP_DELAY}

# start pinging the Open5GS data network for UE1
sudo ip netns exec ue1 ping 10.45.1.1