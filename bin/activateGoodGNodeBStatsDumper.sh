#!/bin/bash
set -e

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh

echo ""
echo "Sleeping for ${GOOD_GNODEB_STATUS_DUMPER_STARTUP_DELAY} seconds to allow the 5G core to start"
echo ""
sleep ${GOOD_GNODEB_STATUS_DUMPER_STARTUP_DELAY}

if [ -f ${RESULTS_FOLDER}/roughData/gNodeB_statistics.jsons ]; then
    sudo rm -f ${RESULTS_FOLDER}/roughData/gNodeB_statistics.json
fi


echo "Lauching GnodeB Stats gatherer"
${SCRIPT_DIR}/dumpGNodeBStats.py --ip 127.0.0.1 --port 55555 --outputFile ${RESULTS_FOLDER}/roughData/gNodeB_statistics.json