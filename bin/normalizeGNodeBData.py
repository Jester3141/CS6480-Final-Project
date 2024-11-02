#!/usr/bin/env python3

import os
import sys
import socket
import json
import argparse
import jsonstream
import tempfile
from datetime import datetime
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4, width=180)

def getEarliestTimestamp(iperfData):
    earliestTimestamp = datetime.now().timestamp()
    for iperfJson in iperfData:
        if earliestTimestamp > iperfJson['timestamp']:
            earliestTimestamp = iperfJson['timestamp']
    return earliestTimestamp

def normalizeGNodeBData(iperfData, earliestTimestamp):
    """
    GNodeB is mostly good but data requires attaching of the UE numb to be really easy to do thigns with.
    """
    print("Received %s jsons" % len(iperfData))
    print("***********************************************************************************")
    ret = []


    for iperfJson in iperfData:
        j = {}
        j['timestamp'] = iperfJson['timestamp'] - earliestTimestamp
        j['ue_list'] = []
        totalDownloadBitrateForAllUEs = 0.0
        totalUploadBitrateForAllUEs = 0.0
        print("----------------------------------------------------------")
        for i in range(0, len(iperfJson["ue_list"])):
            ueContDict = iperfJson["ue_list"][i]
            ueContDict['ue_container']["ue"] = i+1
            totalDownloadBitrateForAllUEs += ueContDict['ue_container']["dl_brate"]
            totalUploadBitrateForAllUEs += ueContDict['ue_container']["ul_brate"]
            ueContDict['ue_container']["total_brate"] = ueContDict['ue_container']["dl_brate"] + ueContDict['ue_container']["ul_brate"]
            j['ue_list'].append(ueContDict)
        j['totals'] = {}
        j['totals']['total_ul_brate'] = totalUploadBitrateForAllUEs
        j['totals']['total_dl_brate'] = totalDownloadBitrateForAllUEs
        j['totals']['total_brate'] = totalDownloadBitrateForAllUEs + totalUploadBitrateForAllUEs
        ret.append(j)


    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='normalizeIperf3Data.py', description='Normalizes a stream of iperf3 json data to a better format')
    parser.add_argument('--input',         required=True, help="The file to read the stream in from")
    parser.add_argument('--output',        required=True, help="the file to write json out to")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"ERROR: specified input file does not exist: {args.input}")
        sys.exit(1)
    
    data = []

    with open(args.input, "r") as read_file:
        data = json.load(read_file)

    #pp.pprint(data)

    earliestTimestamp = getEarliestTimestamp(data)
    print(f"The earliest timestamp is {earliestTimestamp}")
    # write out the earliest timestamp file
    earliestTimestampOutputFile = f"{os.path.dirname(os.path.abspath(args.input))}/earliestTimestamp.json"
    with open(earliestTimestampOutputFile, 'w') as file:
        file.write(json.dumps({"earliestTimestamp": earliestTimestamp}, sort_keys=True, indent=4))


    normalizedData = normalizeGNodeBData(data, earliestTimestamp)
    #pp.pprint(normalizedData)

    formattedOutput = json.dumps(normalizedData, sort_keys=True, indent=4)
    with open(args.output, 'w') as file:
        file.write(formattedOutput)

