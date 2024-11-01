#!/bin/bash
set -e


# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh
source /local/generated/UENUM.sh
source /local/generated/timings.sh

VARNAME=$(echo -e "UE${UENUM}_PACKET_GENERATION_DELAY")
UE_PACKET_GENERATION_DELAY="${!VARNAME}"

VARNAME=$(echo -e "USE_UE${UENUM}")
USE_UE="${!VARNAME}"

if [[ "$USE_UE" == *[fF]alse ]]; then
  echo "UE${UENUM}: was not configured for use.  Not doing anything"
  exit 0
fi


echo ""
echo "UE${UENUM}: Sleeping for ${UE_PACKET_GENERATION_DELAY} seconds to allow the 5G core and GNB to start"
echo ""
sleep ${UE_PACKET_GENERATION_DELAY}

echo ""
echo "UE${UENUM}: Starting UE Ping"
echo ""

# start pinging the Open5GS data network for the UE
ping 10.45.0.1