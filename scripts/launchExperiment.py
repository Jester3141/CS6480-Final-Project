#!/usr/bin/env python3
import sys
import os
import argparse
import shutil
import errno
import subprocess
import yaml


def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='modifyGnbConfig.py', description='Performs modifications to the GNB config file',)
    parser.add_argument('-u', '--user',   required=True, help="The username for the node")
    parser.add_argument('-n', '--experimentNumber',   required=True, help="The experiment number of the nodes")
    args = parser.parse_args()

    print(f"Launching terminator with config file for experiement: {args.experimentNumber}")

    silentremove("hostConfig.yml")
    shutil.copy2("hostConfig.yml.template", "hostConfig.yml")

    subprocess.call(["sed -i -e 's/${EXPERIMENTNUMBER}/%s/g' hostConfig.yml" % args.experimentNumber], shell=True)
    subprocess.call(["sed -i -e 's/${USER}/%s/g' hostConfig.yml" % args.user], shell=True)


    with open("hostConfig.yml", "r") as file:
        data = yaml.safe_load(file)
    


    silentremove("terminatorconfig")
    shutil.copy2("terminatorconfig.template", "terminatorconfig")

    for key, value in data.items():
        subprocess.call(["sed -i -e 's/${%s}/%s/g' terminatorconfig" % (key, value)], shell=True)
    subprocess.call(["sed -i -e 's/${USERNAME}/%s/g' terminatorconfig" % args.user], shell=True)


    subprocess.call(["terminator -g terminatorconfig -l TestRunner"], shell=True)


