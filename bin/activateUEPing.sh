#!/bin/bash
set -e

UE_PING_STARTUP_DELAY=0

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh


echo ""
echo "Sleeping for ${UE_PING_STARTUP_DELAY} seconds to allow the 5G core and GNB to start"
echo ""
sleep ${UE_PING_STARTUP_DELAY}

# start pinging the Open5GS data network for the UE
ping 10.45.0.1