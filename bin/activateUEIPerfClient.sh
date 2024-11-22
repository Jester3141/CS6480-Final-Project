#!/bin/bash
set -e


# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh
source /local/generated/UENUM.sh
source /local/generated/timings.sh

# check if this should be used with this UE
VARNAME=$(echo -e "USE_UE${UENUM}")
USE_UE="${!VARNAME}"

if [[ "$USE_UE" == *[fF]alse ]]; then
  echo "UE${UENUM}: was not configured for use.  Not doing anything"
  exit 0
fi



VARNAME=$(echo -e "UE${UENUM}_PACKET_GENERATION_DELAY")
UE_PACKET_GENERATION_DELAY="${!VARNAME}"


echo ""
echo "UE${UENUM}: Sleeping for ${UE_PACKET_GENERATION_DELAY} seconds to allow the 5G core and GNB to start"
echo ""
sleep ${UE_PACKET_GENERATION_DELAY}


echo ""
echo "UE${UENUM}: Starting UE IPerf Client"
echo ""

sudo mkdir -p ${RESULTS_FOLDER}
sudo chmod a+rwx ${RESULTS_FOLDER}
sudo mkdir -p ${RESULTS_FOLDER}/roughData/
sudo chmod a+rwx ${RESULTS_FOLDER}/roughData/

if [ -f ${RESULTS_FOLDER}/roughData/UE_iperf_results.jsons ]; then
    sudo rm -f ${RESULTS_FOLDER}/roughData/UE_iperf_results.json
fi


# start iperf3 client for UE1 and pass traffic on the downlink
if [[ "$IPERF3_USE_UDP" == "TRUE" ]]; then
  echo "UE${UENUM}: Starting IPerf3 Client (in UDP mode).  Output is being redirected to file so you won't see anything. This is normal."
  iperf3 -c 10.45.0.1 -R --json --logfile ${RESULTS_FOLDER}/roughData/UE_iperf_results.json -p 520${UENUM} -t ${DWELL_DURATION} -u -b ${IPERF3_UDP_TARGET_BANDWIDTH}
else
  echo "UE${UENUM}: Starting IPerf3 Client (in TCP mode).  Output is being redirected to file so you won't see anything. This is normal."
  iperf3 -c 10.45.0.1 -R --json --logfile ${RESULTS_FOLDER}/roughData/UE_iperf_results.json -p 520${UENUM} -t ${DWELL_DURATION}
fi
echo "UE${UENUM}: IPerf3 Client exited"
