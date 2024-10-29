#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh





TerminateUEs
TerminateUEPingers
TerminateIPerf3
