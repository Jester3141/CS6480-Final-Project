#!/bin/bash
set -ex


# Double check that we have properly finished setup and building of the 5g core.
# the easiest way to do this is to check for the presence of the docker executable
if [ ! -f /usr/local/bin/gnb ]; then
    echo "gnb not installed.  This indicates the gnb client is not installed yet"
    echo "You can install it with the following command:"
    echo ""
    echo "sudo ./deploy-srs.sh release_23_11 srsRAN_4G"
    echo ""
    exit 1
fi




# copy the existing gnb conf file to a new one
sudo cp /etc/srsran/gnb.conf /etc/srsran/gnb_good.conf

# Modify the good config file to report statistics
#TODO

# start the Evil gNodeB
sudo gnb -c /etc/srsran/gnb_good.conf
