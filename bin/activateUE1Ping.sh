#!/bin/bash
set -ex

# start pinging the Open5GS data network for UE1
sudo ip netns exec ue1 ping 10.45.1.1