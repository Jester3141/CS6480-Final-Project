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
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

def extractBandwidthInfoFromIperfData(iperfData):
    """
    Iperf data requires some finagling because the timestamp is not embedded with the data point
    """
    pp.pprint(iperfData)
    iperfStartTimestamp = iperfData["start"]["timestamp"]["timesecs"]
    ret = []
    for interval in iperfData["intervals"]:
        p = {}
        p["timestamp"] = iperfStartTimestamp + interval["sum"]["end"]
        p["bits_per_second"] = interval["sum"]["bits_per_second"]
        ret.append(p)
    return ret




def writeGraphWithDataToFile(args, ueNum, gnbData, gnbParameter, ueData, iperfData):
    #pp.pprint(gnbData)
    x = [p["timestamp"] for p in gnbData if "ue_list" in p]
    y = [p["ue_list"][ueNum]["ue_container"][gnbParameter] for p in gnbData if "ue_list" in p]
    #print(x)
    #print(y)
    # plotting the points 
    plt.plot(x, y, label=f"{parameter} vs Time")

    # naming the x axis
    plt.xlabel('Timestamp')
    # naming the y axis
    plt.ylabel(parameter)

    # giving a title to my graph
    plt.title(f"UE {ueNum} - {parameter} vs Time")

    #pp.pprint(ueData)
    uex = [p["timestamp"] for p in ueData]
    uey = [p["gw_container"]["dl_bitrate"] for p in ueData]
    #print(x)
    #print(y)
    # plotting the points
    plt.plot(uex, uey, label=f"dl bbitrate vs Time")


    #pp.pprint(ueData)
    iperfx = [p["timestamp"] for p in iperfData]
    iperfy = [p["bits_per_second"] for p in iperfData]
    #print(x)
    #print(y)
    # plotting the points
    plt.plot(iperfx, iperfy, label=f"iperfbitspersecond")



    # function to show the plot
    # plt.show()
    plt.legend(loc="upper left")
    plt.savefig(f'{args.outputDir}/UE{ueNum}_{parameter}.png')  # Save as PNG file
    plt.clf()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='ConvertDataToImages', description='converts a json file containing the data to plot images',)
    parser.add_argument('-ig',         '--inputGnbJson',   required=True, help="Input json of data from the gNodeB")
    parser.add_argument('-iue',        '--inputUeJson',    required=True, help="Input json of data from the UE")
    parser.add_argument('-iperf',      '--inputIPerfJson', required=True, help="Input json of data from the IPerf")
    parser.add_argument('-o',          '--outputDir',      required=True, help="Output Directory")
    args = parser.parse_args()

    print("Generating images")

    if not os.path.exists(args.inputGnbJson):
        print("Error specified gNodeB input file doesn't exist: %s" % args.inputGnbJson)
        sys.exit(1)

    if not os.path.exists(args.inputUeJson):
        print("Error specified UE input file doesn't exist: %s" % args.inputUeJson)
        sys.exit(1)

    if not os.path.exists(args.inputIPerfJson):
        print("Error specified iperf input file doesn't exist: %s" % args.inputIPerfJson)
        sys.exit(1)

    gNodeBData = loadDataFromJsonFile(args.inputGnbJson)
    ueData = loadDataFromJsonFile(args.inputUeJson)
    iperfData = extractBandwidthInfoFromIperfData(loadDataFromJsonFile(args.inputIPerfJson))
    pp.pprint(iperfData)

    parameters = ["pci",
                  "rnti",
                  "cqi",
                  "ri",
                  "dl_mcs",
                  "dl_brate",
                  "dl_nof_ok",
                  "dl_nof_nok",
                  "dl_bs",
                  "pusch_snr_db",
                  "ul_mcs",
                  "ul_brate",
                  "ul_nof_ok",
                  "ul_nof_nok",
                  "bsr",
                  ]

    for parameter in parameters:
        writeGraphWithDataToFile(args=args,
                                 ueNum=0,
                                 gnbData=gNodeBData,
                                 gnbParameter=parameter,
                                 ueData=ueData,
                                 iperfData=iperfData,
                                 )

    