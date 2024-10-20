#!/bin/bash
set -ex

# start pinging the Open5GS data network for UE3
sudo ip netns exec ue3 ping 10.45.1.1