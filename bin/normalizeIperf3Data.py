#!/usr/bin/env python3

import os
import sys
import socket
import json
import argparse
import jsonstream
import tempfile
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4, width=180)

def normalizeIperfData(iperfData, ueNum):
    """
    Iperf data requires some finagling because the timestamp is not embedded with the data point
    """
    print("Received %s jsons" % len(iperfData))
    print("***********************************************************************************")
    ret = []

    for iperfJson in iperfData:
        print("----------------------------------------------------------")
        pp.pprint(iperfJson)
        if len(iperfJson["intervals"]) == 0:
            continue
        iperfStartTimestamp = iperfJson["start"]["timestamp"]["timesecs"]
        for interval in iperfJson["intervals"]:
            p = {}
            p["timestamp"] = iperfStartTimestamp + interval["sum"]["end"]
            p["ue_list"] = []
            q = {}
            q["ue"] = ueNum
            q["bits_per_second"] = interval["sum"]["bits_per_second"]
            q["bytes"] = interval["sum"]["bytes"]
            q["sender"] = interval["sum"]["sender"]
            c = {}
            c["ue_container"] = q
            p["ue_list"].append(c)
            ret.append(p)
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='normalizeIperf3Data.py', description='Normalizes a stream of iperf3 json data to a better format')
    parser.add_argument('--input',         required=True, help="The file to read the stream in from")
    parser.add_argument('--output',        required=True, help="the file to write json out to")
    parser.add_argument('--ue',            required=True, type=int, help="the UE number that this came from (1-4)")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"ERROR: specified input file does not exist: {args.input}")
        sys.exit(1)
    
    data = []

    with open(args.input, "r") as read_file:
        data = json.load(read_file)

    pp.pprint(data)

    normalizedData = normalizeIperfData(data, ueNum=args.ue)
    pp.pprint(normalizedData)

    formattedOutput = json.dumps(normalizedData, sort_keys=True, indent=4)
    with open(args.output, 'w') as file:
        file.write(formattedOutput)
