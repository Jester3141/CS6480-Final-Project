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
from pprint import PrettyPrinter

try:
    import matplotlib
    import ruamel.yaml
    import jsonstream
except ModuleNotFoundError as ex:
    print('You need matplotlib, ruamel.yaml, and jsonstream to run this.  Run "sudo pip install ruamel.yaml jsonstream matplotlib"')
    sys.exit(1)


pp = PrettyPrinter(indent=4, width=180)

def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

def printExperimentParameters(experiment):
    if " " in experiment['experiment']['name']:
        raise Exception(f"Error experiment name [{experiment['experiment']['name']}]can not have spaces in it.")
    print(f"Experiment: {experiment['experiment']['name']}")
    print(f"              {experiment['experiment']['description']}")
    tests = experiment['experiment']['tests']
    print(f"            # of Test steps :  {len(tests)}")
    print(f"")

    # tests is a list of dicts
    for test in tests:
        testName = list(test.keys())[0]  # there will be only one key
        if " " in testName:
            raise Exception(f"Error experiment name [{testName}]can not have spaces in it.")
        print(f"Test: {testName}\n")
        testParamDict = test[testName]
        print(f"Timings: \n{pp.pformat(testParamDict['timings'])}\n")
        print(f"Good GnodeB Configuration file (applied to the default)\n")
        #print(testParapDict)
        print(f"{yaml.dump(testParamDict['goodGNodeBParameters'])}")
        print(f"")

        if testParamDict['useEvilGNodeB']:
            print(f"Evil GnodeB Configuration file (applied to the default)\n")
            print(f"{yaml.dump(testParamDict['evilGNodeBParameters'])}")
            print(f"")

        print("UEs:")
        uesToUse = testParamDict['uesToUse']
        if len(uesToUse) == 0:
            print(f"Error: not configured to use any UEs")
            sys.exit(1)
        else:
            print(f"   Configured to use the following UE(s):")
            for ueNum in uesToUse:
                print(f"        {ueNum}")

def generateExperimentConfigFiles(experiment):
    generatedBaseFolder = f"{os.path.dirname(os.path.abspath(__file__))}/generated"
    shutil.rmtree(generatedBaseFolder, ignore_errors=True)
    os.makedirs(generatedBaseFolder)

    tests = experiment['experiment']['tests']
    for test in tests:
        testName = list(test.keys())[0]  # there will be only one key
        testParamDict = test[testName]
        testConfigFolder = f"{generatedBaseFolder}/{testName}"
        os.makedirs(testConfigFolder)
        with open(f'{testConfigFolder}/goodGNodeBConfig.yaml', 'w') as file:
            yaml.dump(testParamDict['goodGNodeBParameters'], file)
        if testParamDict['useEvilGNodeB']:
            with open(f'{testConfigFolder}/evilGNodeBConfig.yaml', 'w') as file:
                yaml.dump(testParamDict['evilGNodeBParameters'], file)
        with open(f'{testConfigFolder}/timings.sh', 'w') as file:
            file.write(f"GOOD_GNODEB_STARTUP_DELAY={testParamDict['timings']['goodGNodeBStartupDelay']}\n")
            file.write(f"EVIL_GNODEB_STARTUP_DELAY={testParamDict['timings']['evilGNodeBStartupDelay']}\n")
            file.write(f"USE_EVIL_GNODEB={testParamDict['useEvilGNodeB']}\n")

            file.write(f"UE1_STARTUP_DELAY={testParamDict['timings']['ue1StartupDelay']}\n")
            file.write(f"UE2_STARTUP_DELAY={testParamDict['timings']['ue2StartupDelay']}\n")
            file.write(f"UE3_STARTUP_DELAY={testParamDict['timings']['ue3StartupDelay']}\n")
            file.write(f"UE4_STARTUP_DELAY={testParamDict['timings']['ue4StartupDelay']}\n")

            file.write(f"UE1_PACKET_GENERATION_DELAY={testParamDict['timings']['ue1StartupDelay'] + testParamDict['timings']['ue1PacketGenerationStartupDelay']}\n")
            file.write(f"UE2_PACKET_GENERATION_DELAY={testParamDict['timings']['ue2StartupDelay'] + testParamDict['timings']['ue2PacketGenerationStartupDelay']}\n")
            file.write(f"UE3_PACKET_GENERATION_DELAY={testParamDict['timings']['ue3StartupDelay'] + testParamDict['timings']['ue3PacketGenerationStartupDelay']}\n")
            file.write(f"UE4_PACKET_GENERATION_DELAY={testParamDict['timings']['ue4StartupDelay'] + testParamDict['timings']['ue4PacketGenerationStartupDelay']}\n")

            file.write(f"DWELL_DURATION={testParamDict['timings']['dwellDuration']}\n")
        
            file.write(f"GOOD_GNODEB_STATS_DUMPER_STARTUP_DELAY={testParamDict['timings']['goodGNodeBStatsDumperStartupDelay']}\n")

            for i in range(1,5):  # 1-4
                useUe = i in testParamDict['uesToUse']
                file.write(f"USE_UE{i}={useUe}\n")


def runExperiment(experiment, args):

    tests = experiment['experiment']['tests']
    for test in tests:
        testName = list(test.keys())[0]  # there will be only one key
        testParamDict = test[testName]
        runExperimentTest(testName=testName, testParamDict=testParamDict, args=args)



def runExperimentTest(testName, testParamDict, args):
    print(f"**************************************************************************")
    print(f"**                                                                      **")
    print(f"**            Running experiment {testName}                             **")
    print(f"**                                                                      **")
    print(f"**************************************************************************")

    ue1CompletionDelay = testParamDict['timings']['ue1StartupDelay'] + testParamDict['timings']['ue1PacketGenerationStartupDelay'] + testParamDict['timings']['dwellDuration']
    ue2CompletionDelay = testParamDict['timings']['ue2StartupDelay'] + testParamDict['timings']['ue2PacketGenerationStartupDelay'] + testParamDict['timings']['dwellDuration']
    ue3CompletionDelay = testParamDict['timings']['ue3StartupDelay'] + testParamDict['timings']['ue3PacketGenerationStartupDelay'] + testParamDict['timings']['dwellDuration']
    ue4CompletionDelay = testParamDict['timings']['ue4StartupDelay'] + testParamDict['timings']['ue4PacketGenerationStartupDelay'] + testParamDict['timings']['dwellDuration']
    experimentTime = max(ue1CompletionDelay, ue2CompletionDelay, ue3CompletionDelay, ue4CompletionDelay) + 5

    with open("hostConfig.yml", "r") as file:
        data = yaml.safe_load(file)

    #TODO: ssh config files
    print(f"Copying generated config files over to the nodes")
    ret = subprocess.call([f"{os.path.dirname(__file__)}/scpConfigFiles.sh {testName}"], shell=True)
    if ret == 0:
        print(f"Done copying generated config files over to the nodes")
    else:
        raise Exception("Error: Unable to scp config files to the nodes")


    # generate the terminator launch file
    silentremove("terminatorconfig")
    shutil.copy2("terminatorconfig.template", "terminatorconfig")

    for key, value in data.items():
        subprocess.call(["sed -i -e 's/${%s}/%s/g' terminatorconfig" % (key, value)], shell=True)
    subprocess.call(["sed -i -e 's/${USERNAME}/%s/g' terminatorconfig" % args.user], shell=True)

    # double check that terminator is installed
    ret = subprocess.call(["which terminator"], shell=True)
    if ret != 0:
        print(f'ERROR: you must have terminator installed to run this.  Install it with the command "sudo apt install -y terminator".')
        sys.exit(1)

    # launch terminator (in the background)
    termShortCommandLine = 'terminator -g terminatorconfig -l TestRunner'
    terminatorCommandLine = "/bin/sh -c '%s'" % termShortCommandLine
    terminatorArgs = shlex.split(terminatorCommandLine)
    print("terminatorArgs = %s" % terminatorArgs)
    terminatorProcess = subprocess.Popen(terminatorArgs)

    # wait for a while to get results
    print(f"Waiting {experimentTime} seconds for experiment to run")
    time.sleep(experimentTime)


    # Kill (nicely) all running experiment processes on the nodes
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
    
    # collect results and place them into the correct locations

    testResultsFolder = f"{args.resultsFolder}/{testName}"
    print(f"Collecting results and placing them into {testResultsFolder}")
    os.makedirs(testResultsFolder, exist_ok=True)
    subprocess.call([f"{os.path.dirname(__file__)}/collectResults.sh {testResultsFolder}"], shell=True)
    shutil.copy(args.experimentDefinitionFile, f"{args.resultsFolder}/experiment.yaml")
    print(f"Results have been collected and are in: {testResultsFolder}")





def generateGraphsFromExperimentResults(args):
    print("Writing graphs for experiment to file")
    subprocess.call([f"{os.path.dirname(__file__)}/writeExperimentGraphs.py -i {args.resultsFolder}"], shell=True)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='modifyGnbConfig.py', description='Performs modifications to the GNB config file',)
    parser.add_argument('-u', '--user',   required=True, help="The username for the node")
    parser.add_argument('-n', '--experimentName',   required=True, help="The experiment name")
    parser.add_argument('-e', '--experimentDefinitionFile',   required=True, help="The yaml defining the experiment to run")
    parser.add_argument('-p', '--project',   required=True, help="The powder project the experiment is running under")
    parser.add_argument('-r', '--resultsFolder',   required=False, default=os.path.abspath(f'{os.path.dirname(__file__)}/../results/{datetime.now().strftime("%Y-%m-%d_%H%M%S")}'),
                        help="The folder to put results in.  Defaults to a dated subfolder inside this projects results folder")
    args = parser.parse_args()

    print(f"Launching terminator with config file for experiement: {args.experimentName}")
    print(f"Placing results in: {args.resultsFolder}")


    silentremove("hostConfig.sh")
    silentremove("hostConfig.yml")
    shutil.copy2("hostConfig.yml.template", "hostConfig.yml")
    subprocess.call(["sed -i -e 's/${%s}/%s/g' hostConfig.yml" % ('USER', args.user)], shell=True)
    subprocess.call(["sed -i -e 's/${%s}/%s/g' hostConfig.yml" % ('EXPERIMENTNAME', args.experimentName)], shell=True)
    subprocess.call(["sed -i -e 's/${%s}/%s/g' hostConfig.yml" % ('PROJECT', args.project)], shell=True)



    print(f"Loading experiment definition yaml from {args.experimentDefinitionFile}")
    
    experimentDefinition = {}
    with open(args.experimentDefinitionFile, "r") as file:
        experimentDefinition = yaml.safe_load(file)


    printExperimentParameters(experimentDefinition)

    # now we need to generate the configuration files that will be scp'd to each node.
    generateExperimentConfigFiles(experimentDefinition)

    # run the experiment
    runExperiment(experimentDefinition, args)

    # generate graphs from experiment
    generateGraphsFromExperimentResults(args=args)

    print(f"Test complete. You can find your results in {args.resultsFolder}")
