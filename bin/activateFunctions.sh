
GOOD_GNODEB_STARTUP_DELAY=10

GOOD_GNODEB_STATUS_DUMPER_STARTUP_DELAY=18
IPERF3_STARTUP_DELAY=15

UE1_STARTUP_DELAY=15
UE1_PING_STARTUP_DELAY=20
UE1_IPERF_CLIENT_STARTUP_DELAY=35

RESULTS_GATHERING_DELAY=60


RESULTS_FOLDER=/results/


# Checks to ensure that the 5G core is setup and ready to go
CheckFor5GCoreSetup () {
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

}





# Checks to ensure that the 4G GNB is setup and ready to go
CheckFor4gGNBSetup () {
    # Double check that we have properly finished setup and building of the 4G GNB.
    # the easiest way to do this is to check for the presence of the gnb executable
    if [ ! -f /etc/srsran/gnb.conf ]; then
        echo "gnb not installed.  This indicates the gnb client is not installed yet"
        echo "You can install it with the following command:"
        echo ""
        echo "sudo ./deploy-srs.sh release_23_11 srsRAN_4G"
        echo ""
        exit 1
    fi


}



# Terminates all running GNodeB Stats gathering scripts
TerminateGNodeBStatsGatherers () {
    echo "Terminating the gNodeB stats gatherers"
    (set +e ; ps -ef | grep "dumpGNodeBStats.py" | awk '{print $2}' | xargs kill -SIGINT)
    echo "The gNodeB stats gatherers have been terminated"
}

# Terminates all running GNodeBs
TerminateGNodeBs () {
    echo "Terminating the gNodeBs"
    (set +e ; ps -ef | grep "gnb" | awk '{print $2}' | sudo xargs kill -SIGINT)
    echo "The gNodeBs have been terminated"
}

# Terminates all running UEs
TerminateUEs () {
    echo "Terminating the UEs"
    (set +e ; ps -ef | grep "srsue" | awk '{print $2}' | sudo xargs kill -SIGINT)
    echo "The UEs have been terminated"
}

# Terminates all running pingers
TerminateUEPingers () {
    echo "Terminating the UE Pingers"
    (set +e ; ps -ef | grep "ping" | awk '{print $2}' | sudo xargs kill -SIGINT)
    echo "The UE Pingers have been terminated"
}

# Terminates all running iperf3
TerminateIPerf3 () {
    echo "Terminating the IPerf3 clients and servers"
    (set +e ; ps -ef | grep "iperf3" | awk '{print $2}' | xargs kill -SIGINT)
    echo "The IPerf3 clients and servers have been terminated"
}

# Terminates all running 5GCores
Terminate5GCore () {
    echo "Terminating the 5G Core"
    sudo docker rm $(sudo docker stop $(sudo docker ps -a -q --filter ancestor=docker-5gc))
    echo "5G Core Terminated"
}

# Terminates all services
TerminateAllServices () {
    echo "Terminating All Services"
    TerminateUEPingers
    TerminateIPerf3
    TerminateUEs
    TerminateGNodeBStatsGatherers
    TerminateGNodeBs
    Terminate5GCore
    echo "All Services have been terminated"
}