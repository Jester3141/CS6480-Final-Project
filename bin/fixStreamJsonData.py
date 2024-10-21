#!/usr/bin/env python3

import os
import sys
import socket
import json
import argparse
import jsonstream




if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='fixStreamJsonData.py', description='formats a stream of json data to be a valid json')
    parser.add_argument('--input',         required=True, help="The file to read the stream in from")
    parser.add_argument('--output',        required=True, help="the file to write json out to")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"ERROR: specified input file does not exist: {args.input}")
        sys.exit(1)

    outputContents = ""
    with open(args.input, 'r') as file:
        f = jsonstream.load(file)
        outputContents = list(f)
    
    formattedOutput = json.dumps(outputContents, sort_keys=True, indent=4)
    with open(args.output, 'w') as file:
        file.write(formattedOutput)
