#!/usr/bin/env python3
import sys
import os
import argparse
import io

try:
    import ruamel.yaml
except ModuleNotFoundError as ex:
    print('You need ruamel.yaml to run this.  Run "python -m pip install ruamel.yaml"')
    sys.exit(1)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='modifyGnbConfig.py', description='Performs modifications to the GNB config file',)
    parser.add_argument('-f',    '--file',   required=True, help="The input file")
    parser.add_argument('--metricsIpAddr',   required=False, default=None, help="If set, will set the metrics addr in the config file")
    parser.add_argument('--metricsPort',     required=False, default=None, help="If set, set the port in the config file")
    parser.add_argument('--testMode',        required=False, action="store_true", default=None, help="If set, enables test mode in the config file")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"ERROR: specified input file does not exist: {args.file}")
        sys.exit(1)
    
    fileContents = ""
    
    yaml = ruamel.yaml.YAML()  # defaults to round-trip if no parameters given

    with open(args.file, 'r') as file:
        fileContents = file.read()
        code = yaml.load(fileContents)

        ## Modfications here:

        if args.metricsIpAddr is not None:
            code['metrics']['addr'] = args.metricsIpAddr

        if args.metricsPort is not None:
            code['metrics']['port'] = int(args.metricsPort)

        if args.testMode is not None:
            if 'test_mode' not in code:
                code['test_mode'] = {}
            code['test_mode']['enable'] = True

    buf = io.BytesIO()
    yaml.dump(code, buf)
    newFileContents = buf.getvalue()
    # print(newFileContents)

    print(f"Writing modifed config file: {args.file}")
    with open(args.file, 'wb') as file:
       file.write(newFileContents)

    
