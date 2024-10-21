#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh




echo ""
echo "Sleeping for ${RESULTS_GATHERING_DELAY} seconds to allow the test to run"
echo ""
sleep ${RESULTS_GATHERING_DELAY}


TerminateAllServices

echo "Sleeping for 5 seconds to ensure items have exited"
sleep 5

echo "Need to format the results files to ensure they are json"

# the gnode stats are already in a good format
cp ${RESULTS_FOLDER}/roughData/gNodeB_statistics.json ${RESULTS_FOLDER}/data/

# the iperf stats are already in a good format
cp ${RESULTS_FOLDER}/roughData/UE1_iperf_results.json ${RESULTS_FOLDER}/data/

# The UE1 metrics are anoying in that they are a stream of json documents and need some conversion
${SCRIPT_DIR}/fixStreamJsonData.py --input ${RESULTS_FOLDER}/roughData/UE1_metrics.json --output ${RESULTS_FOLDER}/data/UE1_metrics.json




set -x
# Create output images
${SCRIPT_DIR}/convertDataToImages.py --inputGnbJson ${RESULTS_FOLDER}/data/gNodeB_statistics.json \
                                     --inputUeJson ${RESULTS_FOLDER}/data/UE1_metrics.json \
                                     --inputIPerfJson ${RESULTS_FOLDER}/data/UE1_iperf_results.json \
                                     --outputDir ${RESULTS_FOLDER}