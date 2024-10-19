#!/bin/bash
set -ex



# copy the existing gnb conf file to a new one
sudo cp /etc/srsran/gnb.conf /etc/srsran/gnb_evil.conf

# Modify the evil config file to be truly evil
#TODO

# start the Evil gNodeB
sudo gnb -c /etc/srsran/gnb_evil.conf


