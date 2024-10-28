#!/usr/bin/env python3

import argparse
import sys
import json
import os
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4, width=180)

try:
    import matplotlib
    import matplotlib.pyplot as plt
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
    x = [p["timestamp"] for p in data if "ue_list" in p]
    # print(data)
    y = []
    for p in data:
        if "ue_list" not in p:
            continue
        for ueCont in p['ue_list']:
            # print(ueCont)
            if 'ue_container' in ueCont and 'ue' in ueCont['ue_container'] and ueCont['ue_container']['ue'] == ueNum:
                y.append(ueCont['ue_container'][paramName])
    return x,y

def getXYTotalsDataFromData(data, paramName):
    print("getXYTotalsDataFromData")
    x = [p["timestamp"] for p in data]
    # print(data)
    y = []
    for p in data:
        if "totals" not in p:
            continue
        y.append(p['totals'][paramName])
    return x,y


def writeGraphWithDataToFile(args, filename, gNodeBParameter, gNodeBDisplayName, ueParameter, ueDisplayName, gNodeBUeNum=1):
    #pp.pprint(gnbData)
    plt.clf()

    if gNodeBParameter.startswith("total_"):
        print(f"Adding GNB totals data to graph for {gNodeBParameter}")
        x,y = getXYTotalsDataFromData(args.gNodebStatistics, gNodeBParameter)
    else:
        print(f"Adding GNB data for UE {gNodeBUeNum} to graph for {gNodeBParameter}")
        x,y = getXYDataFromData(args.gNodebStatistics, gNodeBParameter, gNodeBUeNum)

    # plotting the points 
    plt.plot(x, y, label=f"{gNodeBDisplayName} vs Time")

    # naming the x axis
    plt.xlabel('Time')
    # naming the y axis
    plt.ylabel(gNodeBDisplayName)

    # giving a title to my graph
    plt.title(f"TODO Graph Title")

    for ueNum in range(0,4):   # 1-4
            x,y = getXYDataFromData(args.ueIperfStatistics[ueNum], ueParameter, ueNum+1)
            if len(y) == 0:
                # We don't have any data for this UE.  Skip it
                continue
            print(f"Adding UE{ueNum+1} data to graph for {ueParameter}")
            calcUeDisplayName = ueDisplayName.replace("<UE>", "UE%s" % (ueNum+1))
            plt.plot(x, y, label=f"{calcUeDisplayName} vs Time")



    # function to show the plot
    # plt.show()
    plt.legend(loc="upper left")
    plt.savefig(f'{args.outputDir}/{filename}')  # Save as PNG file
    plt.clf()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='ConvertDataToImages', description='converts a json file containing the data to plot images',)
    parser.add_argument('-i',          '--inputDir',      required=True, help="Input Directory containing 'gNodeB_stats_normalized.json` and one or more UE iperf files of the format 'UE1_iperf_results_normalized.json'")
    parser.add_argument('-o',          '--outputDir',      required=True, help="Output Directory")
    args = parser.parse_args()

    print("Generating images")

    gNodeBFilename = f"{os.path.abspath(args.inputDir)}/gNodeB_stats_normalized.json"
    ue1IperfFilename = f"{os.path.abspath(args.inputDir)}/UE1_iperf_results_normalized.json"
    ue2IperfFilename = f"{os.path.abspath(args.inputDir)}/UE2_iperf_results_normalized.json"
    ue3IperfFilename = f"{os.path.abspath(args.inputDir)}/UE3_iperf_results_normalized.json"
    ue4IperfFilename = f"{os.path.abspath(args.inputDir)}/UE4_iperf_results_normalized.json"

    if not os.path.exists(gNodeBFilename):
        print("Error: the gnodeB normailzed stats file doesn't exist: %s    (This is required)" % gNodeBFilename)
        sys.exit(1)

    if not os.path.exists(ue1IperfFilename):
        print("Error: the UE1 normalized stats file doesn't exist: %s    (This is required)" % ue1IperfFilename)
        sys.exit(1)

    if not os.path.exists(ue2IperfFilename):
        print("Info: the UE2 normalized stats file doesn't exist: %s    (UE2 data won't be included)" % ue2IperfFilename)

    if not os.path.exists(ue3IperfFilename):
        print("Info: the UE3 normalized stats file doesn't exist: %s    (UE3 data won't be included)" % ue3IperfFilename)

    if not os.path.exists(ue4IperfFilename):
        print("Info: the UE4 normalized stats file doesn't exist: %s    (UE4 data won't be included)" % ue4IperfFilename)

    args.gNodebStatistics = loadDataFromJsonFile(gNodeBFilename)
    args.ue1IperfStatistics = loadDataFromJsonFile(ue1IperfFilename)
    args.ue2IperfStatistics = loadDataFromJsonFile(ue2IperfFilename)
    args.ue3IperfStatistics = loadDataFromJsonFile(ue3IperfFilename)
    args.ue4IperfStatistics = loadDataFromJsonFile(ue4IperfFilename)
    args.ueIperfStatistics = [args.ue1IperfStatistics, args.ue2IperfStatistics, args.ue3IperfStatistics, args.ue4IperfStatistics]


    print("****************************************************************************************************")
    writeGraphWithDataToFile(args=args,
                             filename="dl_bitrate.png",
                             gNodeBParameter="dl_brate",
                             gNodeBDisplayName="gNodeB DL bitrate",
                             gNodeBUeNum=2,
                             ueParameter="bits_per_second",
                             ueDisplayName="<UE> bit per second"
                             )
    
    print("****************************************************************************************************")
    writeGraphWithDataToFile(args=args,
                             filename="ul_bitrate.png",
                             gNodeBParameter="ul_brate",
                             gNodeBDisplayName="gNodeB UL bitrate",
                             gNodeBUeNum=2,
                             ueParameter="bits_per_second",
                             ueDisplayName="<UE> bit per second"
                             )

    print("****************************************************************************************************")
    writeGraphWithDataToFile(args=args,
                             filename="total.png",
                             gNodeBParameter="total_brate",
                             gNodeBDisplayName="gNodeB UL bitrate",
                             ueParameter="bits_per_second",
                             ueDisplayName="<UE> bit per second"
                             )
    print("****************************************************************************************************")
    