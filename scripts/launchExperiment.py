#!/usr/bin/env python3
import sys
import os
import argparse
import shutil
import errno
import subprocess
import yaml
import time
import shlex
import signal
import psutil
from datetime import datetime


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
    parser.add_argument('-r', '--resultsFolder',   required=False, default=os.path.abspath(f'{os.path.dirname(__file__)}/../results/{datetime.now().strftime("%Y-%m-%d_%H%M%S")}'),
                        help="The folder to put results in.  Defaults to a dated subfolder inside this projects results folder")
    args = parser.parse_args()

    print(f"Launching terminator with config file for experiement: {args.experimentNumber}")
    print(f"Placing results in: {args.resultsFolder}")

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

    termShortCommandLine = 'terminator -g terminatorconfig -l TestRunner'
    terminatorCommandLine = "/bin/sh -c '%s'" % termShortCommandLine
    terminatorArgs = shlex.split(terminatorCommandLine)
    print("terminatorArgs = %s" % terminatorArgs)
    terminatorProcess = subprocess.Popen(terminatorArgs)

    experimentTime = 60
    print(f"Waiting {experimentTime} seconds for experiment to run")
    time.sleep(experimentTime)


    print(f"Killing experiment processes")
    subprocess.call([f"{os.path.dirname(__file__)}/sshAndKillProcesses.sh"], shell=True)

    killWaitTime = 10
    print(f"Waiting {killWaitTime} seconds for processes to finish exiting")
    time.sleep(killWaitTime)
    print(f"Killing the experiment terminator window with pid {terminatorProcess.pid}")
    terminatorProcess.kill()
    terminatorProcess.wait()
    # terminator may not be close at this point, so we do one more. round
    for proc in psutil.process_iter():
        if proc.name() == "terminator":
            if "terminatorconfig" in proc.cmdline() and 'TestRunner' in proc.cmdline():
                proc.kill()

    print(f"Collecting results and placing them into {args.resultsFolder}")
    os.makedirs(args.resultsFolder, exist_ok=True)
    subprocess.call([f"{os.path.dirname(__file__)}/collectResults.sh {args.resultsFolder}"], shell=True)
    print(f"Results have been collected and are in: {args.resultsFolder}")



