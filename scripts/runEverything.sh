#!/bin/bash
set -e


./launchExperiment.py -u u0204096 -n u0204096-230929 -p TDDInterfere -e experiments.withandwithoutevil.yaml
./launchExperiment.py -u u0204096 -n u0204096-230929 -p TDDInterfere -e experiments.gaintest.yaml
./launchExperiment.py -u u0204096 -n u0204096-230929 -p TDDInterfere -e experiments.gainwithoutoverlaptest.yaml
./launchExperiment.py -u u0204096 -n u0204096-230929 -p TDDInterfere -e experiments.gaintenmhzbuffertest.yaml
./launchExperiment.py -u u0204096 -n u0204096-230929 -p TDDInterfere -e experiments.arfcntesttest.yaml
./launchExperiment.py -u u0204096 -n u0204096-230929 -p TDDInterfere -e experiments.gaptest.yaml
./launchExperiment.py -u u0204096 -n u0204096-230929 -p TDDInterfere -e experiments.tddtest.yaml