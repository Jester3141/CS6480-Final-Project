#!/bin/bash
set -e

#TODO: set back to false eventually
DEBUG=true

echo "scping configuraion files to the nodes"
# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

GENERATED_CONFIG_DIR=${SCRIPT_DIR}/generated/
TESTNAME=$1

if [ ${#TESTNAME} -gt 0 ]; then
    echo "scping configuraion files for test: ${TESTNAME} to the nodes"
else
  echo "Usage: scpConfigFiles <TESTNAME>"
  exit 1
fi



cat ${SCRIPT_DIR}/hostConfig.yml | awk '{split($0,a,": "); printf "export %s=\"%s\"\n", a[1], a[2];}' > ${SCRIPT_DIR}/hostConfig.sh
source ${SCRIPT_DIR}/hostConfig.sh

source ${GENERATED_CONFIG_DIR}/${TESTNAME}/timings.sh

NUC_HOSTNAMES=("${NUC_1_HOSTNAME}" "${NUC_2_HOSTNAME}" "${NUC_3_HOSTNAME}" "${NUC_4_HOSTNAME}")
GNB_HOSTNAMES=("${GOOD_GNB_HOSTNAME}" "${EVIL_GNB_HOSTNAME}" "${UNUSED_GNB_3_HOSTNAME}" "${UNUSED_GNB_4_HOSTNAME}")
ALL_HOSTNAMES=("${FIVEG_CORE_HOSTNAME}" "${GNB_HOSTNAMES[@]}" "${NUC_HOSTNAMES[@]}")

# remove any exising generated config files
for HOSTNAME in ${ALL_HOSTNAMES[@]}; do
    echo ""
    echo "Removing any existing config files and results from ${HOSTNAME}"
    ssh -o StrictHostKeyChecking=no ${USER}@${HOSTNAME} -t 'sudo rm -rf /local/generated; sudo rm -rf /results; mkdir -p /local/generated'
    if [ "$DEBUG" = true ] ; then
        echo "To ensure the latest state, scping the repo bin folder to ${HOSTNAME}"
        rsync -az ${SCRIPT_DIR}/../bin/* ${USER}@${HOSTNAME}:/local/repository/bin/
    fi
done

# copy config files to the 5G core node
echo "Copying the Good gNodeB config files to ${FIVEG_CORE_HOSTNAME}"
scp ${GENERATED_CONFIG_DIR}/${TESTNAME}/timings.sh ${USER}@${FIVEG_CORE_HOSTNAME}:/local/generated/

# copy config files to the good GNodeB
echo "Copying the Good gNodeB config files to ${GOOD_GNB_HOSTNAME}"
scp ${GENERATED_CONFIG_DIR}/${TESTNAME}/goodGNodeBConfig.yaml ${GENERATED_CONFIG_DIR}/${TESTNAME}/timings.sh ${USER}@${GOOD_GNB_HOSTNAME}:/local/generated/

# copy config files to the evil GNodeB
if [[ "$USE_EVIL_GNODEB" == *[fF]alse ]]; then
  echo "Evil gNodeB was not configured for use.  Not copying gnb config files"
  scp ${GENERATED_CONFIG_DIR}/${TESTNAME}/timings.sh ${USER}@${EVIL_GNB_HOSTNAME}:/local/generated/
else
  echo "Copying the Evil gNodeB config files to ${EVIL_GNB_HOSTNAME}"
  scp ${GENERATED_CONFIG_DIR}/${TESTNAME}/evilGNodeBConfig.yaml ${GENERATED_CONFIG_DIR}/${TESTNAME}/timings.sh ${USER}@${EVIL_GNB_HOSTNAME}:/local/generated/
fi


# each NUC just needs a file that tells it what UE it is.  
for NUC_HOSTNAME_INDEX in ${!NUC_HOSTNAMES[@]}; do
    NUC_HOSTNAME=${NUC_HOSTNAMES[NUC_HOSTNAME_INDEX]}
    UENUM=$((NUC_HOSTNAME_INDEX+1))

    VARNAME=$(echo -e "USE_UE${UENUM}")
    USE_UE="${!VARNAME}"

    echo "Copying the nuc config files to ${NUC_HOSTNAME}"
    echo "UENUM=${UENUM}" > .nucid
    chmod u+x .nucid
    scp ${SCRIPT_DIR}/.nucid ${USER}@${NUC_HOSTNAME}:/local/generated/UENUM.sh
    scp  ${GENERATED_CONFIG_DIR}/${TESTNAME}/timings.sh ${USER}@${NUC_HOSTNAME}:/local/generated/
    rm -f .nucid

    # if there were any other config files that the NUCs needed, we could add them here.
done

