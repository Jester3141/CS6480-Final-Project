#!/usr/bin/env python3

import argparse
import sys
import json
import os

try:
    import matplotlib
    import matplotlib.pyplot as plt
except ModuleNotFoundError as ex:
    print('You need matplotlib to run this.  Run "python -m pip install matplotlib"')
    sys.exit(1)


def loadDataFromFile(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data


def writeGraphWithDataToFile(data, ueNum, parameter):
    x = [p["timestamp"] for p in data]
    y = [p["ue_list"][ueNum]["ue_container"][parameter] for p in data]
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

    # function to show the plot
    # plt.show()
    plt.savefig(f'UE{ueNum}_{parameter}.png')  # Save as PNG file

    plt.clf()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='ConvertDataToImages',
                                     description='converts a json file containing the data to plot images',)
    parser.add_argument('-i', '--inputFile', required=True, help="Input file of data")
    args = parser.parse_args()

    print("Generating images")

    if not os.path.exists(args.inputFile):
        print("Error specified input file doesn't exist: %s" % args.inputFile)
        sys.exit(1)

    data = loadDataFromFile(args.inputFile)
    #print(data)

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
        writeGraphWithDataToFile(data=data, 
                                 ueNum=0, 
                                 parameter=parameter,
                                 )

    