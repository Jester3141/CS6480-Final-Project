#!/bin/bash
set -ex

# sudo ./deploy-srs.sh release_24_04 srsRAN_Project


# create a network namespace for the UE
sudo ip netns add ue1 || true
sudo ip netns add ue2 || true
sudo ip netns add ue3 || true
sudo ip netns add ue4 || true

# Double check that we have properly finished setup and building of the 5g core.
# the easiest way to do this is to check for the presence of the docker executable
if [ ! -f /usr/bin/docker ]; then
    echo "Docker not installed.  This indicates the 5G core is not installed."
    echo "You can install it with the following command:"
    echo ""
    echo "sudo ./deploy-srs.sh release_24_04 srsRAN_Project"
    echo ""
    exit 1
fi


# start 5gc container
sudo docker compose -f /opt/srsRAN_Project/docker/docker-compose.yml up 5gc