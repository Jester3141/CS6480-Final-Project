#!/bin/bash
set -e


# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh
source /local/generated/UENUM.sh
source /local/generated/timings.sh

# check if this should be used on this UE
VARNAME=$(echo -e "USE_UE${UENUM}")
USE_UE="${!VARNAME}"

if [[ "$USE_UE" == *[fF]alse ]]; then
  echo "UE${UENUM}: was not configured for use.  Not doing anything"
  exit 0
fi

VARNAME=$(echo -e "UE${UENUM}_STARTUP_DELAY")
UE_STARTUP_DELAY="${!VARNAME}"

echo ""
echo "UE${UENUM}: Sleeping for ${UE_STARTUP_DELAY} seconds to allow the 5G core and GNB to start"
echo ""
sleep ${UE_STARTUP_DELAY}



echo ""
echo "UE${UENUM}: Starting UE"
echo ""

# turn on the modem
sudo sh -c "chat -t 1 -sv '' AT OK 'AT+CFUN=1' OK < /dev/ttyUSB2 > /dev/ttyUSB2"


# launch the the quectel UE app
sudo quectel-CM -s internet -4

