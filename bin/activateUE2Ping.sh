#!/bin/bash
set -ex

# start pinging the Open5GS data network for UE2
sudo ip netns exec ue2 ping 10.45.1.1