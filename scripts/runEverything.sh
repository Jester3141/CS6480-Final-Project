#!/bin/bash
set -e


#./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.withandwithoutevil.yaml
#./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.gaintest.yaml
#./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.gainwithoutoverlaptest.yaml
#./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.gaintenmhzbuffertest.yaml
#./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.arfcntest.yaml
#./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.gaptest.yaml
#./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.tddtest.yaml


# ./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.gainfivemhzoverlaptest.yaml
# ./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.gaintenmhzoverlaptest.yaml
#./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.gaintwentymhzoverlaptest.yaml

# ./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.tddwithoutoverlaptest.yaml
#./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.tddfivemhzoverlaptest.yaml
# ./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.tddtenmhzoverlaptest.yaml
# ./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.tddtwentymhzoverlaptest.yaml
# ./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.tddtenmhzbuffertest.yaml

# ./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.gaintest.udp.yaml
# ./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.withandwithoutevil.udp.yaml


# Things to try....
#  UDP test.
#  

# new experiments
./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.tddtenmhzoverlaptest.yaml
./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.tddtwentymhzoverlaptest.yaml
./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.tddtenmhzbuffertest.yaml

# experimetns to redo
./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.gaintwentymhzoverlaptest.yaml
./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.gainfivemhzoverlaptest.yaml
./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.tddtest.yaml
./launchExperiment.py -u u0204096 -n u0204096-232008 -p TDDInterfere -e experiments.tddfivemhzoverlaptest.yaml

#ssh u0204096@u0204096-232008.TDDInterfere.emulab.net