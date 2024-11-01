#!/bin/bash
set -e

DIR=$1

echo "Collecting results and putting them in ${DIR}"
# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


cat ${SCRIPT_DIR}/hostConfig.yml | awk '{split($0,a,": "); printf "export %s=\"%s\"\n", a[1], a[2];}' > ${SCRIPT_DIR}/hostConfig.sh
source ${SCRIPT_DIR}/hostConfig.sh

NUC_HOSTNAMES=("${NUC_1_HOSTNAME}" "${NUC_2_HOSTNAME}" "${NUC_3_HOSTNAME}" "${NUC_4_HOSTNAME}")


if [ ! -d ${DIR} ]; then
  echo "Results directory doesn't exist: ${DIR}"
  exit 1
fi

# create the results sub folders
mkdir -p ${DIR}/data/
mkdir -p ${DIR}/roughData/
mkdir -p ${DIR}/config/
mkdir -p ${DIR}/config/goodGNodeB/
mkdir -p ${DIR}/config/evilGNodeB/

set +e
# scp the gNodeB stats from the good gnodeb
scp ${USER}@${GOOD_GNB_HOSTNAME}:/results/roughData/gNodeB_statistics.json ${DIR}/roughData/gNodeB_statistics.json.raw

# scp the gNodeB config from the good gnodeb (so we know what we launched with)
scp ${USER}@${GOOD_GNB_HOSTNAME}:/local/generated/goodGNodeBConfig.yaml ${DIR}/config/goodGNodeB/

# scp the gNodeB config from the evil gnodeb (so we know what we launched with)
scp ${USER}@${EVIL_GNB_HOSTNAME}:/local/generated/evilGNodeBConfig.yaml ${DIR}/config/evilGNodeB/


for NUC_HOSTNAME_INDEX in ${!NUC_HOSTNAMES[@]}; do
    NUC_HOSTNAME=${NUC_HOSTNAMES[NUC_HOSTNAME_INDEX]}
    UENUM=$((NUC_HOSTNAME_INDEX+1))
    scp ${USER}@${NUC_HOSTNAME}:/results/roughData/UE_iperf_results.json ${DIR}/roughData/UE${UENUM}_iperf_results.json.raw
done

set -e

#########################################################################################################
##                                                                                                     ##
## At this point the files have been copied.  Now we need to fix the data to a nice normalized format  ##
##                                                                                                     ##
#########################################################################################################

# normalize gNodeB Statistics
if [ -f ${DIR}/roughData/gNodeB_statistics.json.raw ]; then
    echo -e "Normalizing gNodeB Statistics"
    ${SCRIPT_DIR}/../bin/normalizeGNodeBData.py --input ${DIR}/roughData/gNodeB_statistics.json.raw --output ${DIR}/data/gNodeB_statistics_normalized.json
fi

# normalize UE Statistics
for UENUM in {1..4}; do
    if [ -f ${DIR}/roughData/UE${UENUM}_iperf_results.json.raw ]; then
        echo -e "Normalizing UE${UENUM} Statistics"
        ${SCRIPT_DIR}/../bin/fixStreamJsonData.py --input ${DIR}/roughData/UE${UENUM}_iperf_results.json.raw --output ${DIR}/roughData/UE${UENUM}_iperf_results.json
        ${SCRIPT_DIR}/../bin/normalizeIperf3Data.py --input ${DIR}/roughData/UE${UENUM}_iperf_results.json --output ${DIR}/data/UE${UENUM}_iperf_results_normalized.json --ue ${UENUM}
    fi
done
