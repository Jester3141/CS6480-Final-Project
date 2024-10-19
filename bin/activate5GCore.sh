#!/bin/bash
set -ex


# create a network namespace for the UE
sudo ip netns add ue1
sudo ip netns add ue2
sudo ip netns add ue3
sudo ip netns add ue4

# start 5gc container
sudo docker compose -f /opt/srsRAN_Project/docker/docker-compose.yml up 5gc