#!/bin/bash
set -ex

# start iperf3 client for UE1 and pass traffic on the downlink
sudo ip netns exec ue3 iperf3 -c 10.45.1.1 -R