#!/bin/bash
set -ex

# start iperf3 server within the 5gc docker container
sudo docker exec -it open5gs_5gc iperf3 -s