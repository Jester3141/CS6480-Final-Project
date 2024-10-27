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



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='fixStreamJsonData.py', description='formats a stream of json data to be a valid json')
    parser.add_argument('--input',         required=True, help="The file to read the stream in from")
    parser.add_argument('--output',        required=True, help="the file to write json out to")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"ERROR: specified input file does not exist: {args.input}")
        sys.exit(1)
    
    # going to do this in 2 phases.
    # phase 1 read the file and write it back out to a temp file.
    #    during this phase we will squelch any text between the json outputs (like what iperf likes to put)
    lines = []
    cleanedLines = []
    with open(args.input, 'r') as file:
        lines = file.readlines()
        insideJSON = False
        for n in range(0, len(lines)):
            if lines[n].startswith("}"):
                insideJSON = False
            elif lines[n].startswith("{"):
                insideJSON = True
            else:
                if not insideJSON:
                    # print("Troublesome line")
                    continue
            cleanedLines.append(lines[n])

    tempfilename = ""
    with tempfile.NamedTemporaryFile() as fp:
        tempFilename = fp.name
        with open(tempFilename, 'w') as file:
            file.writelines(cleanedLines)



        # Phase 2:  read in the now properly formatted json stream file and dump out a pure json file
        outputContents = ""
        with open(tempFilename, 'r') as file:
            f = jsonstream.load(file)
            outputContents = list(f)
        
        formattedOutput = json.dumps(outputContents, sort_keys=True, indent=4)
        with open(args.output, 'w') as file:
            file.write(formattedOutput)
