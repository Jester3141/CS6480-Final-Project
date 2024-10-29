#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh



# NOTE: the 5g core runs as a system service (not docker) and doesn't need to be killed

TerminateIPerf3
