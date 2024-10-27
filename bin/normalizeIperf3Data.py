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

    pp.pprint(data)

    # TODO finish this.
