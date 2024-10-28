#!/bin/bash
set -e

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


cat ${SCRIPT_DIR}/hostConfig.yml | awk '{split($0,a,": "); printf "export %s=\"%s\"\n", a[1], a[2];}' > ${SCRIPT_DIR}/hostConfig.sh
source ${SCRIPT_DIR}/hostConfig.sh  

# go throug each host killing running processes.