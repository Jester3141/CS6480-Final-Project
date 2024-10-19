#!/bin/bash
set -ex


# copy the existing gnb conf file to a new one
sudo cp /etc/srsran/gnb.conf /etc/srsran/gnb_good.conf

# Modify the good config file to report statistics
#TODO

# start the Evil gNodeB
sudo gnb -c /etc/srsran/gnb_good.conf
