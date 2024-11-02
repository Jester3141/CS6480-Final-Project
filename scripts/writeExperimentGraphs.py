#!/usr/bin/env python3

import argparse
import sys
import json
import os
import yaml
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4, width=180)

try:
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.ticker as tkr 
except ModuleNotFoundError as ex:
    print('You need matplotlib to run this.  Run "python -m pip install matplotlib"')
    sys.exit(1)


def loadDataFromJsonFile(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        data = json.load(file)
        return data


def getXYDataFromData(data, paramName, ueNum):
    x = []
    # print(data)
    y = []
    for p in data:
        if "ue_list" not in p or len(p['ue_list']) == 0:
            continue
        for ueCont in p['ue_list']:
            # print(ueCont)
            if 'ue_container' in ueCont and 'ue' in ueCont['ue_container'] and ueCont['ue_container']['ue'] == ueNum:
                y.append(ueCont['ue_container'][paramName])
                x.append(p["timestamp"])
    return x,y

def getXYTotalsDataFromData(data, paramName):
    # print("getXYTotalsDataFromData")
    x = []
    # print(data)
    y = []
    for p in data:
        if "ue_list" not in p or len(p['ue_list']) == 0:
            continue
        if "totals" not in p:
            continue
        y.append(p['totals'][paramName])
        x.append(p["timestamp"])
    return x,y




def getXYDataForPlotParameter(param, args):
    '''
    Plot param name is a bar separated string consiting of 3 parts.

    1: The test name
    2: A string indicating which file to pull the stat from (GoodGNodeB, UE1, UE2, UE3, or UE4)
    3: The parameter name inside the file to graph
    '''
    print(f"Attempting to load x,y data for {param}")
    x = []
    y = []
    sourceNameToFilenameDict = {'GoodGNodeB': 'gNodeB_statistics_normalized.json',
                                'UE1': 'UE1_iperf_results_normalized.json',
                                'UE2': 'UE2_iperf_results_normalized.json',
                                'UE3': 'UE3_iperf_results_normalized.json',
                                'UE4': 'UE4_iperf_results_normalized.json',
                                }
    thirdNameToUENumDict = {'UE1': 1,
                            'UE2': 2,
                            'UE3': 3,
                            'UE4': 4,
                            }

    # do a bit of input validation:
    splits = param.split('|')
    if len(splits) != 3 and len(splits) != 4:
        raise Exception(f"Error: Plot param was not in the correct format: {param}")
    testName = splits[0].strip()
    sourceName = splits[1].strip()
    third = splits[2].strip()
    paramName = third
    if len(testName) == 0 or len(sourceName) == 0 or len(third) == 0:
        raise Exception(f"Error: One of the parameters items was of zero length: {param}")
    
    resultsFolder = os.path.abspath(args.inputDir)
    if not os.path.exists(resultsFolder):
        raise Exception(f"Error: The specified results folder doesn't exist: {resultsFolder}")
    
    testFolder = f"{resultsFolder}/{testName}"
    if not os.path.exists(testFolder):
        raise Exception(f"Error: The folder for the specified test doesn't exist: {testFolder}")
    
    if sourceName not in sourceNameToFilenameDict:
        raise Exception(f"Error: you specified a source name of '{sourceName}' but this is not a possible choice.  Correct choices are {list(sourceNameToFilenameDict.keys())}")
    
    sourceFilename = f"{testFolder}/data/{sourceNameToFilenameDict[sourceName]}"
    if not os.path.exists(sourceFilename):
        raise Exception(f"Error: The source file doesn't exist: {sourceFilename}")
    
    ueNum = 1
    if sourceName == "GoodGNodeB" and third in thirdNameToUENumDict:
        # the 4th split is the parameter name
        if len(splits) != 4:
            raise Exception(f"Error: Plot param was not in the correct format: {param}")
        paramName = splits[3].strip()
        ueNum = thirdNameToUENumDict[third]

    # now we are reasonably certain that we can look in the file and get some reasonable results.
    jsonData = loadDataFromJsonFile(sourceFilename)
    if paramName.startswith("total_"):
        x,y = getXYTotalsDataFromData(data=jsonData, paramName=paramName)
    else:
        x,y = getXYDataFromData(data=jsonData, paramName=paramName, ueNum=ueNum)


    return x, y
    





def outputAllGraphs(experiment, args):

    graphs = experiment['experiment']['graphs']
    for graph in graphs:
        graphName = list(graph.keys())[0]  # there will be only one key
        graphParamDict = graph[graphName]
        graphFilename = graphParamDict['filename']
        graphTitle = graphParamDict['graphTitle']
        outputGraph(graphName=graphName, graphFilename=graphFilename, graphTitle=graphTitle, graphParamDict=graphParamDict, args=args)


def outputGraph(graphName, graphFilename, graphTitle, graphParamDict, args):
    print(f"\n\nOutputting graph {graphName} with title {graphTitle} to file {graphFilename}")
    pp.pprint(graphParamDict)

    graphOutputDirectory = f"{os.path.abspath(args.inputDir)}/graphs/"
    os.makedirs(graphOutputDirectory, exist_ok=True)


    plt.clf()

    # output overall graph items
    plt.xlabel(graphParamDict['xaxisLabel'])
    plt.ylabel(graphParamDict['yaxisLabel'])
    plt.title(graphTitle)

    if len(graphParamDict['plots']) > 0:
        for plot in graphParamDict['plots']:
            plotName = list(plot.keys())[0]  # there will be only one key
            paramDict = plot[plotName]
            x,y = getXYDataForPlotParameter(param=paramDict['plotParameter'], args=args)
            plt.plot(x, y, label=paramDict['plotName'])

    if 'yaxisType' in graphParamDict and graphParamDict['yaxisType'] == "bytes":
        ax = plt.gca()  # get the axes object
        ax.yaxis.set_major_formatter(tkr.FuncFormatter(sizeof_fmt))

    if 'legendLocation' in graphParamDict and len(graphParamDict['legendLocation']) > 0:
        plt.legend(loc=graphParamDict['legendLocation'])
    else:
        plt.legend(loc="best")
    
    plt.gcf().set_tight_layout(True)

    plt.savefig(f'{graphOutputDirectory}/{graphFilename}')  # Save as PNG file
    plt.clf()


def sizeof_fmt(x, pos):
    # matlapb formatter for bytes.
    if x<0:
        return ""
    for x_unit in ['bps', 'kbps', 'Mbps', 'Gbps', 'Tbps']:
        if x < 1024.0:
            return "%3.1f %s" % (x, x_unit)
        x /= 1024.0



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='writeExperimentGraphs.py', description='takes in a results directory and creates the graphs',)
    parser.add_argument('-i',          '--inputDir',      required=True, help="Input Directory (the one containing the experiment.yaml)")
    args = parser.parse_args()

    experimentDefinitionFile = f"{os.path.abspath(args.inputDir)}/experiment.yaml"
    print(f"Loading experiment configuration from {experimentDefinitionFile}")

    experimentDefinition = {}
    with open(experimentDefinitionFile, "r") as file:
        experimentDefinition = yaml.safe_load(file)

    outputAllGraphs(experiment=experimentDefinition, args=args)
    sys.exit(1)
