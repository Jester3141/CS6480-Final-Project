#!/bin/bash
set -ex

# bring in common functions
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source ${SCRIPT_DIR}/activateFunctions.sh


# ensure we are ready to run the 5G core
CheckFor5GCoreSetup


# create a network namespace for the UE
sudo ip netns add ue1 || true
sudo ip netns add ue2 || true
sudo ip netns add ue3 || true
sudo ip netns add ue4 || true


# start 5gc container
sudo docker compose -f /opt/srsRAN_Project/docker/docker-compose.yml up 5gc