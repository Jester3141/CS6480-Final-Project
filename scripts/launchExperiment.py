#!/usr/bin/env python3
import sys
import os
import argparse
import shutil
import errno
import subprocess


def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='modifyGnbConfig.py', description='Performs modifications to the GNB config file',)
    parser.add_argument('--host',   required=True, help="The host where the experiment will run")
    parser.add_argument('--user',   required=True, help="The username for the node")
    args = parser.parse_args()

    print(f"Launching terminator with config file for host: {args.host}")

    silentremove("terminatorconfig")
    shutil.copy2("terminatorconfig.template", "terminatorconfig")
    subprocess.call(["sed -i -e 's/${HOSTNAME}/%s/g' terminatorconfig" % args.host], shell=True)
    subprocess.call(["sed -i -e 's/${USERNAME}/%s/g' terminatorconfig" % args.user], shell=True)


    subprocess.call(["terminator -g terminatorconfig -l TestRunner"], shell=True)


