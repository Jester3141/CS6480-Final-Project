#!/bin/bash
set -e

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


cat ${SCRIPT_DIR}/hostConfig.yml | awk '{split($0,a,": "); printf "export %s=\"%s\"\n", a[1], a[2];}' > ${SCRIPT_DIR}/hostConfig.sh
source ${SCRIPT_DIR}/hostConfig.sh  


NUC_HOSTNAMES=("${NUC_1_HOSTNAME}" "${NUC_2_HOSTNAME}" "${NUC_3_HOSTNAME}" "${NUC_4_HOSTNAME}")
GNB_HOSTNAMES=("${GOOD_GNB_HOSTNAME}" "${EVIL_GNB_HOSTNAME}" "${UNUSED_GNB_3_HOSTNAME}" "${UNUSED_GNB_4_HOSTNAME}")


# go through each host killing running processes.

echo -e "Sending SIGINT any to running Iperf3 clients on the NUCS"
for NUC_HOSTNAME in ${NUC_HOSTNAMES[@]}; do
    echo -e "Terminating any running UE pingers on ${NUC_HOSTNAME}"
    set +e
    ssh  -o StrictHostKeyChecking=no ${USER}@${NUC_HOSTNAME} "sudo /local/repository/bin/terminateNucUeServices.sh"
    set -e
done
echo -e "Done Killing IPerf3 Clients and pingers on NUCS"

echo -e "Sending SIGINT any to running iperf3 servers on the 5G Core node: ${FIVEG_CORE_HOSTNAME}"
set +e
ssh  -o StrictHostKeyChecking=no ${USER}@${FIVEG_CORE_HOSTNAME} "sudo /local/repository/bin/terminate5GCoreServices.sh"
set -e
echo -e "Done Killing IPerf3 server on the 5GCore"


echo -e "Sending SIGINT any to running gNodeB Status Gatherers and gNodeB on the gnuradio comp nodes"
for GNB_HOSTNAME in ${GNB_HOSTNAMES[@]}; do
    echo -e "Terminating any running gNodeB Stats Gatherers or gNodeB applications on ${GNB_HOSTNAME}"
    set +e
    ssh  -o StrictHostKeyChecking=no ${USER}@${GNB_HOSTNAME} "sudo /local/repository/bin/terminateGnbServices.sh"
    set -e
    exit 0
done
echo -e "Done Killing gNodeB and gNodebStatsGatherers"
