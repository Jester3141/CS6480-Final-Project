#!/usr/bin/env python

import os

import geni.portal as portal # type: ignore
import geni.rspec.pg as rspec
import geni.rspec.igext as IG
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab
import geni.rspec.emulab.pnext as PN
import geni.rspec.emulab.spectrum as spectrum

tourDescription = """
### srsRAN 5G using the POWDER Indoor OTA Lab with an EVIL GNB

This profile instantiates an experiment for running srsRAN_Project 5G with COTS UEs in standalone mode using resources in the POWDER indoor over-the-air (OTA) lab. The indoor OTA lab includes:

- 4x NI X310 SDRs, each with a UBX-160 daughter card occupying channel 0. The TX/RX and RX2 ports on this channel are connected to broadband antennas. The SDRs are connected via fiber to near-edge compute resources.
- 4x Intel NUC compute nodes, each equipped with a Quectel RM500Q-GL 5G module that has been provisioned with a SIM card. The NUCs are also equipped with NI B210 SDRs.

You can find a diagram of the lab layout here: [OTA Lab Diagram](https://gitlab.flux.utah.edu/powderrenewpublic/powder-deployment/-/raw/master/diagrams/ota-lab.png)

The following will be deployed:

- Server-class compute node (d430) with running the Open5GS 5G core network
- Server-class compute node (d740) with GnuRadio and a fiber connection to an X310 and srsRAN_Project for use as a gNodeB
- Server-class compute node (d740) with GnuRadio and a fiber connection to an X310 and srsRAN_Project for use as a EVIL gNodeB (running in test mode)
- 2x Server-class compute node (d430) with with fiber connections to a X310.  (not used, but reserved so there will be no cross experiment interference)
- 4x NUC compute nodes, each with a COTS 5G module and supporting tools

Note: This profile currently defaults to using the 3430-3470 MHz spectrum range and you need an approved reservation for this spectrum in order to use it. It's also strongly recommended that you include the following necessary resources in your reservation to gaurantee their availability at the time of your experiment:

"""

tourInstructions = """

# Documentation of various interfaces

This section describes various interaces

## gNodeB Configuration

The gNodeB application can take in one or more yml files with the `-c` flag.  For each setting in the file, it overrides the settings from the previous files.

For example, consider the command:
```bash
sudo /var/tmp/srsRAN_Project/build/apps/gnb/gnb -c /var/tmp/etc/srsran/gnb_rf_x310_tdd_n78_40mhz.yml -c /local/generated/goodGNodeBConfig.yaml
```

The first `-c` sets up all parameters to the default x310 profile contained in `/var/tmp/etc/srsran/gnb_rf_x310_tdd_n78_40mhz.yml`.

The second `-c` only contains:

```yaml
metrics:
  addr: 127.0.0.1
  enable_json_metrics: true
  port: 55555
```
It only overides a few settings.




## Getting GNB Metrics

Metrics will be output to the console by default.  

The items received by the stats are described here:  https://docs.srsran.com/projects/project/en/latest/user_manuals/source/console_ref.html#manual-console-ref

Console output will look liek this:

```
          |--------------------DL---------------------|-------------------------UL------------------------------
 pci rnti | cqi  ri  mcs  brate   ok  nok  (%)  dl_bs | pusch  rsrp  mcs  brate   ok  nok  (%)    bsr    ta  phr
   1 4601 |  15   1   21    10k   13    3  18%      3 |  65.5   ovl   26    28k   14    0   0%     53   0us  n/a
   1 4601 |  15   1   27   2.5k    3    0   0%      0 |  65.5   ovl   28   6.5k    4    0   0%      0   0us  n/a
   1 4601 |  15   1    0      0    0    0   0%      0 |   n/a   n/a    0      0    0    0   0%      0   0us  n/a
   1 4601 |  15   1    0      0    0    0   0%      0 |   n/a   n/a    0      0    0    0   0%      0   0us  n/a
   1 4601 |  15   1    0      0    0    0   0%      0 |   n/a   n/a    0      0    0    0   0%      0   0us  n/a
   1 4601 |  15   1    0      0    0    0   0%      0 |   n/a   n/a    0      0    0    0   0%      0   0us  n/a
   1 4601 |  15   1    0      0    0    0   0%      0 |   n/a   n/a    0      0    0    0   0%      0   0us  n/a
   1 4601 |  15   1    0      0    0    0   0%      0 |   n/a   n/a    0      0    0    0   0%      0   0us  n/a
   1 4601 |  15   1    0      0    0    0   0%      0 |   n/a   n/a    0      0    0    0   0%      0   0us  n/a
   1 4601 |  15   1    0      0    0    0   0%      0 |   n/a   n/a    0      0    0    0   0%      0   0us  n/a
   1 4601 |  15   1    0      0    0    0   0%      0 |   n/a   n/a    0      0    0    0   0%      0   0us  n/a
```

* **pci**: Physical Cell Identifier https://www.sharetechnote.com/html/Handbook_LTE_PCI.html
* **rnti**: Radio Network Temporary Identifier (UE identifier) https://www.sharetechnote.com/html/5G/5G_RNTI.html
* **cqi**: Channel Quality Indicator reported by the UE (1-15) https://www.sharetechnote.com/html/Handbook_LTE_CQI.html
* **ri**: Rank Indicator as reported by the UE https://www.sharetechnote.com/html/Handbook_LTE_RI.html
* **mcs**: Modulation and coding scheme (0-28) https://www.sharetechnote.com/html/5G/5G_MCS_TBS_CodeRate.html
* **brate**: Bitrate (bits/sec)
* **ok**: Number of packets successfully sent
* **nok**: Number of packets dropped
* **(%)**: % of packets dropped
* **dl_bs**: Downlink Buffer Status, data waiting to be transmitted as reported by the gNB (bytes)
* **pusch**: PUSCH SINR (Signal-to-Interference-plus-Noise Ratio)
* **rsrp**: Reference Signal Received Power https://www.sharetechnote.com/html/5G/5G_PowerDefinition.html
* **bsr**: Buffer Status Report, data waiting to be transmitted as reported by the UE (bytes) https://www.sharetechnote.com/html/Handbook_LTE_BSR.html
* **ta**: Timing Advance in microseconds https://www.sharetechnote.com/html/5G/5G_TimingAdvance.html
* **phr**: Power Headroom as reported by the UE https://www.sharetechnote.com/html/Handbook_LTE_PHR.html




### GNB Metrics output as JSON file


To output gNodeB json metrics you will need to set the following settings
```yml
metrics:
  enable_json_metrics: true            # Optional BOOLEAN (false). Enables JSON metrics reporting. Supported: [false, true].
  addr: 127.0.0.1                       # Optional TEXT:IPV4 (127.0.0.1). Sets the metrics address. Supported: IPV4 address.
  port: 55555                           # Optional UINT. Sets the metrics UPD port. Supported: [0 - 65535].
```

Once the GNB is running we can connect to the port specified `55555` in the example above and will receive a stream of json objects.  The code below will do this and will output a json list of these metrics dicts to the `gnb_metrics.json` file when it exits.

```python
#!/usr/bin/env python3


import socket
import json
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='dumpGNodeBStats.py', description='streams in performance metrics from a gnb',)
    parser.add_argument('--ip',         required=True, help="ip address of the host to listen to")
    parser.add_argument('--port',       required=True, type=int, help="the port to connect to")
    parser.add_argument('--outputFile', required=True, help="the file to write the statistics to")
    args = parser.parse_args()

        
    

    UDP_IP = args.ip   # IP address to bind to (localhost in this case)
    UDP_PORT = args.port       # Port to bind to

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the IP address and port
    sock.bind((UDP_IP, UDP_PORT))

    print("UDP Receiver started...")

    received_data = []

    try:
        while True:
            # Receive message from the sender
            data, addr = sock.recvfrom(1024)
            
            # Decode the received message as JSON
            try:
                json_data = json.loads(data.decode('utf-8'))
                # Print the received JSON data
                print("Received JSON:", json_data)
                received_data.append(json_data)
            except json.JSONDecodeError:
                print("Received data is not in JSON format:", data.decode('utf-8'))

    except KeyboardInterrupt:
        # Save received data to a file
        filename = args.outputFile
        with open(filename, "w") as file:
            json.dump(received_data, file)
        print(f"Received data saved to {filename}. Exiting...")

# based off of  https://docs.srsran.com/projects/project/en/latest/user_manuals/source/outputs.html#json-metrics
```

The written file will contain a list of json metircs that look like this

```json
{
  "timestamp": 1700671417.005,
  "ue_list": [
    {
      "ue_container": {
        "pci": 1,
        "rnti": 17921,
        "cqi": 15,
        "ri": 1,
        "dl_mcs": 27,
        "dl_brate": 291680.0,
        "dl_nof_ok": 352,
        "dl_nof_nok": 0,
        "dl_bs": 0,
        "pusch_snr_db": 24.025097,
        "ul_mcs": 26,
        "ul_brate": 12838928.0,
        "ul_nof_ok": 431,
        "ul_nof_nok": 0,
        "bsr": 0
      }
    }
  ]
}
```




Need to figure out how to run the EVIL gNB.  Some kind of a boolean flag.  Read the documentation....


## Evil gNodeB

To enable test mode you must have settings like this

```yml

amf:
  no_core: true

test_mode:
  test_ue:
    cqi: 15
    nof_ues: 4
    pdsch_active: true
    pusch_active: true
    ri: 1
    rnti: 68

```
NOTE: In the `amf` section add a line that says `no_core: true`.  This allows the evil GNB operate without a connection to the 5g core



If you have more than one radio attached to the machine, you might also possibly need to reconfigure the radio.

Run `ifconfig` and get the ip address of the x310 radio that you want to use for the gnb.  Then reconfigure the `ru_sdr` section appropriately.

For example, if my 2nd x310 radio had an ip address of `192.168.20.2`, I would modify the device_args to be the correct address

```yml
ru_sdr:
  device_driver: uhd
  device_args: type=n3xx, addr=192.168.20.2,send_frame_size=8000,recv_frame_size=8000
  tx_gain: 50
  rx_gain: 50
  srate:  30.72
  sync: external
  clock: external
  time_alignment_calibration: 0
  lo_offset: 45
```

## Running an experiment

You will need to either be running this from a linux machine or a WSL that is running a X server.

First we need to install required packages with the following 4 commands:
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y python3-pip terminator gedit git
sudo pip install ruamel.yaml jsonstream matplotlib
```

Then test to ensure that your X server is started by running:

```bash
terminator
```
That should pop up a terminator window

![asdf](images/terminator.png){width="400px"}

If you've got all that, in theory your ready to run.

Check out the code and cd into the directory.

```bash
git clone https://github.com/Jester3141/CS6480-Final-Project
cd CS6480-Final-Project/scripts
```

Next, you will need an experiment yaml file.  
```bash
cp experiments.template.yaml myexperiment.yaml
```
Edit this file and provide whatever parameters you desire.  More about this file will be said in the next section.

Launch an experiment with this profile.  Take note of the experiment number from powder.  The is a 6 digit number at the end of the name.  For example if my experiment name was `u0204096-227153`, then `227153` would be my experiment number.

Once the experiment is running and all startup scripts have completed, then you can launch the experiment with the following (Replacing the `<ITEM>` with its corresponding value)
```bash
./launchExperiment.py -u <USERNAME> -n <EXPERIMENT_NAME> -p <PROJECT_NAME> -e <EXPERIMENT_YAML_FILENAME>

# for example
./launchExperiment.py -u u0204096 -n u0204096-227153 -p TDDInterfere -e experiments.withandwithoutevil.yaml
```

The test will run for a while getting everything setup.  After a while it will launch a terminator window.

![asdf](images/running_experiment.png)
Once the test finishes, you will find results in the `<GITCHECKOUTDIR>/results/<DATE>/` folder

Please note that the gNodeB configuration files that were used during a test as well as the experiment yaml file
will be copied to the results folder.  This is useful as you can see what settings your results were for.



## Experiment config file

The experiement yaml file allows you to run 1 or more tests serially (one after the other).  See the following files for examples of usage:

The `scripts/experiments.template.yaml` has an example of pretty much all parameters.  One test uses a evil gNodeB and the other doesn't.  The one that does't instantiates 4 UES, where the first one only does one.  Not much experimentation here, but at least shows the syntax.

The `scripts/experiments.withandwithoutevil.yaml` uses a single UE to record download bandwidth.  The only difference
here is one has an evil gNodeB started.

The `scripts/experiments.gaintest.yaml` uses a single UE and runs the experiment 5 times.  The only difference is the ru_sdr's gain  set to 10, 20, 30, 40, and 50 db gain for the evil gNodeB.

### Timings Section

The timing section is required and all parameters in the examples must be present.  If you are not using a parameter it still needs to be included but will be ignored

```yaml
timings: # these are some delay values before starting up things
    goodGNodeBStartupDelay: 5  # from launch, how long to wait (in seconds) before starting the good gNode B
    evilGNodeBStartupDelay: 30   # from launch, how long to wait (in seconds) before starting the evil gNode B (if configured to use)

    ue1StartupDelay: 10  # from launch, how long to wait (in seconds) before starting UE 1
    ue1PacketGenerationStartupDelay: 30  # How long to wait for startup (ue1StartupDelay + ue1PacketGenerationStartupDelay)
    
    ue2StartupDelay: 12  # from launch, how long to wait (in seconds) before starting UE 2
    ue2PacketGenerationStartupDelay: 30  # How long to wait for startup (ue2StartupDelay + ue2PacketGenerationStartupDelay)
    
    ue3StartupDelay: 14  # from launch, how long to wait (in seconds) before starting UE 3
    ue3PacketGenerationStartupDelay: 30  # How long to wait for startup (ue3StartupDelay + ue3PacketGenerationStartupDelay)
    
    ue4StartupDelay: 16  # from launch, how long to wait (in seconds) before starting UE 4
    ue4PacketGenerationStartupDelay: 30  # How long to wait for startup (ue4StartupDelay + ue4PacketGenerationStartupDelay)
    
    goodGNodeBStatsDumperStartupDelay: 44  # from launch, how long to wait (in seconds) before starting the good gNode B stats dumper.
    dwellDuration: 30 # How long (in seconds) will the iperf generators run for
```

### Good gNodeB Experiment section

Everything in the `goodGNodeBParameters` section will be output to a yml and used when starting the good gNodeB.
Items under these section will override the default .yml config files for the good gnb.  The defaults can be found in `scripts/gnb_rf_x310_tdd_n78_40mhz.yml`

```yaml
goodGNodeBParameters:  # everything in here will be added to the good gNodeB's config file
    metrics:
        addr: 127.0.0.1
        port: 55555
        enable_json_metrics: true
```

### Evil gNodeB Experiment section

Everything in the `evilGNodeBParameters` section will be output to a yml and used when starting the evil gNodeB.
Items under these section will override the default .yml config files for the evil gnb.  The defaults can be found in `scripts/gnb_rf_x310_tdd_n78_40mhz.yml`
```yaml
useEvilGNodeB: true # whether or not to start the evil gNodeB
evilGNodeBParameters:  # everything in here will be added to the evil gNodeB's config file
    metrics:
        addr: 127.0.0.1
        port: 55556
        enable_json_metrics: true
    amf:
        no_core: true
    test_mode:
        test_ue:
            rnti: 0x44
            ri: 1 # Set to 2 or 4 for 2 layer or 4 layer MIMO operation
            cqi: 15
            nof_ues: 4
            pusch_active: true
            pdsch_active: true
```
or if not using the evil gNodeB
```yaml
useEvilGNodeB: false # whether or not to start the evil gNodeB
```

### UE(s) experiment section
In the UEs section you may indicate that you want to use between 1 and 4 UES.
```yaml
uesToUse:  # Use one or more UEs.  Just use the lower numbers first.
    - 1
    - 2
    - 3
    - 4
```




### graphs

The graphs section allow you to indicate that you would like 1 or more graphs output to disk.  They will be put in the ```<RESULTS>/graphs``` subfolder.

For example,  The `experiments.gaintest.yaml` experiment runs 5 tests with various gains.  We would like to see the difference between them in graph form.  Therefore we add a section like this:

```yaml
graphs:
    - graph1:
        filename: testplot.png
        graphTitle: UE Download bandwidth
        xaxisLabel: Time
        yaxisLabel: bitrate
        yaxisType: bytes # optional param.  If bytes, will display y axis in MB/s type format
        legendLocation: best # optional param.  default: best.  Valid options are the location string defined here: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html
        plots:
            - plot1:
                plotName: evil gNodeB gain 10
                # all graphs are plotted with time on the x axis
                plotParameter: test1|UE1|bits_per_second
            - plot2:
                plotName: evil gNodeB gain 20
                # all graphs are plotted with time on the x axis
                plotParameter: test2|UE1|bits_per_second
            - plot3:
                plotName: evil gNodeB gain 30
                # all graphs are plotted with time on the x axis
                plotParameter: test3|UE1|bits_per_second
            - plot4:
                plotName: evil gNodeB gain 40
                # all graphs are plotted with time on the x axis
                plotParameter: test4|UE1|bits_per_second
            - plot5:
                plotName: evil gNodeB gain 50
                # all graphs are plotted with time on the x axis
                plotParameter: test5|UE1|bits_per_second
```
This indicates that we are going to have a single output graph with 5 plots on that graph.

When specifying the `plotParameter`, UE items are specified in this format:

```
<TESTNAME>|<UENAME>|<PARAMETER>
```
In the above example I am graphing `bits_per_second` for `UE1` for each of the tests that were ran.

For gNodeB stats, the format is slighly more complicated as it has total status (total for all UEs) and per UE stats.
```
<TESTNAME>|GoodGNodeB|<UENAME>|<PARAMETER>
<TESTNAME>|GoodGNodeB|<TOTAL_PARAMETER>
```

For example if I wanted to plot the `total_dl_brate` for all UEs in `test1`, I would use `test1|GoodGNodeB|total_dl_brate`.  

If I wanted the `dl_brate` for `UE1` in `test1`, I would use `test1|GoodGNodeB|UE1|dl_brate`


![asdf](images/exampleplot.png)
"""

BIN_PATH = "/local/repository/bin"
ETC_PATH = "/local/repository/etc"
UBUNTU_IMG = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD"
COTS_UE_IMG = "urn:publicid:IDN+emulab.net+image+PowderTeam:cots-jammy-image"
COMP_MANAGER_ID = "urn:publicid:IDN+emulab.net+authority+cm"
DEFAULT_SRSRAN_HASH = "4ac5300d4927b5199af69e6bc2e55d061fc33652"
OPEN5GS_DEPLOY_SCRIPT = os.path.join(BIN_PATH, "deploy-open5gs.sh")
SRSRAN_DEPLOY_SCRIPT = os.path.join(BIN_PATH, "deploy-srsran.sh")


def x310_node_pair(idx, compute_node_type, x310_radio, site):
    node = request.RawPC("{}-gnuradio-comp".format(x310_radio))
    node.Site(site)
    #node.component_manager_id = COMP_MANAGER_ID
    node.hardware_type = compute_node_type

    if params.sdr_compute_image:
        node.disk_image = params.sdr_compute_image
    else:
        node.disk_image = UBUNTU_IMG

    node_radio_if = node.addInterface("usrp_if")
    node_radio_if.addAddress(rspec.IPv4Address("192.168.40.1", "255.255.255.0"))

    radio_link = request.Link("radio-link-{}".format(idx))
    radio_link.Site(site)
    radio_link.bandwidth = 10*1000*1000
    radio_link.addInterface(node_radio_if)

    radio = request.RawPC("{}-gnb-sdr".format(x310_radio))
    radio.Site(site)
    radio.component_id = x310_radio
    #radio.component_manager_id = COMP_MANAGER_ID
    radio_link.addNode(radio)

    nodeb_cn_if = node.addInterface("nodeb-cn-if")
    nodeb_cn_if.addAddress(rspec.IPv4Address("192.168.1.{}".format(idx + 2), "255.255.255.0"))
    cn_link.addInterface(nodeb_cn_if)

    if params.srsran_commit_hash:
        srsran_hash = params.srsran_commit_hash
    else:
        srsran_hash = DEFAULT_SRSRAN_HASH

    cmd = "{} '{}'".format(SRSRAN_DEPLOY_SCRIPT, srsran_hash)
    node.addService(rspec.Execute(shell="bash", command=cmd))
    node.addService(rspec.Execute(shell="bash", command="/local/repository/bin/tune-sdr-iface.sh"))

def b210_nuc_pair(b210_node):
    node = request.RawPC("{}-cots-ue".format(b210_node))
    node.Site("UEs")
    #node.component_manager_id = COMP_MANAGER_ID
    node.component_id = b210_node
    node.disk_image = COTS_UE_IMG
    node.addService(rspec.Execute(shell="bash", command="/local/repository/bin/module-off.sh"))
    node.addService(rspec.Execute(shell="bash", command="/local/repository/bin/update-udhcpc-script.sh"))
    node.addService(rspec.Execute(shell="bash", command="sudo apt install -y iperf3"))

pc = portal.Context()

node_types = [
    ("d430", "Emulab, d430"),
    ("d740", "Emulab, d740"),
]

# pc.defineParameter(
#     name="sdr_nodetype",
#     description="Type of compute node paired with the SDRs",
#     typ=portal.ParameterType.STRING,
#     defaultValue=node_types[1],
#     legalValues=node_types
# )

# pc.defineParameter(
#     name="cn_nodetype",
#     description="Type of compute node to use for CN node (if included)",
#     typ=portal.ParameterType.STRING,
#     defaultValue=node_types[0],
#     legalValues=node_types
# )

pc.defineParameter(
    name="sdr_compute_image",
    description="Image to use for compute connected to SDRs",
    typ=portal.ParameterType.STRING,
    defaultValue="",
    advanced=True
)

pc.defineParameter(
    name="srsran_commit_hash",
    description="Commit hash for srsRAN",
    typ=portal.ParameterType.STRING,
    defaultValue="",
    advanced=True
)

indoor_ota_x310s = [
    ("ota-x310-1",
     "USRP X310 #1"),
    ("ota-x310-2",
     "USRP X310 #2"),
    ("ota-x310-3",
     "USRP X310 #3"),
    ("ota-x310-4",
     "USRP X310 #4"),
]
pc.defineParameter(
    name="x310_good_radio",
    description="X310 Radio for the good gNodeB",
    typ=portal.ParameterType.STRING,
    defaultValue=indoor_ota_x310s[0],
    legalValues=indoor_ota_x310s
)

pc.defineParameter(
    name="x310_evil_radio",
    description="X310 Radio for the EVIL gNodeB",
    typ=portal.ParameterType.STRING,
    defaultValue=indoor_ota_x310s[1],
    legalValues=indoor_ota_x310s
)

pc.defineParameter(
    name="x310_unused_radio_1",
    description="X310 Radio 1 that will be reserved but not used",
    typ=portal.ParameterType.STRING,
    defaultValue=indoor_ota_x310s[2],
    legalValues=indoor_ota_x310s
)

pc.defineParameter(
    name="x310_unused_radio_2",
    description="X310 Radio 2 that will be reserved but not used",
    typ=portal.ParameterType.STRING,
    defaultValue=indoor_ota_x310s[3],
    legalValues=indoor_ota_x310s
)

indoor_ota_nucs = [
    ("ota-nuc{}".format(i), "Indoor OTA nuc{} with B210 and COTS UE".format(i)) for i in range(1, 5)
]

# pc.defineStructParameter(
#     name="ue_nodes",
#     description="Indoor OTA NUC with COTS UE (can't be the same as gNodeB node!)",
#     defaultValue=[{ "node_id": "ota-nuc1" }],
#     multiValue=True,
#     min=1,
#     max=4,
#     members=[
#         portal.Parameter(
#             "node_id",
#             "Indoor OTA NUC",
#             portal.ParameterType.STRING,
#             indoor_ota_nucs[0],
#             indoor_ota_nucs
#         )
#     ]
# )

pc.defineStructParameter(
    "freq_ranges", "Frequency Ranges To Transmit In",
    defaultValue=[{"freq_min": 3430.0, "freq_max": 3470.0}],
    multiValue=True,
    min=0,
    multiValueTitle="Frequency ranges to be used for transmission.",
    members=[
        portal.Parameter(
            "freq_min",
            "Frequency Range Min",
            portal.ParameterType.BANDWIDTH,
            3550.0,
            longDescription="Values are rounded to the nearest kilohertz."
        ),
        portal.Parameter(
            "freq_max",
            "Frequency Range Max",
            portal.ParameterType.BANDWIDTH,
            3600.0,
            longDescription="Values are rounded to the nearest kilohertz."
        ),
    ]
)

params = pc.bindParameters()
pc.verifyParameters()
request = pc.makeRequestRSpec()

role = "cn"

# Good GnB
good_cn_node = request.RawPC("goodcn5g")
good_cn_node.Site("Good gNodeB")
#good_cn_node.component_manager_id = COMP_MANAGER_ID
good_cn_node.hardware_type = node_types[0][0]
good_cn_node.disk_image = UBUNTU_IMG
cn_if = good_cn_node.addInterface("cn-if")
cn_if.addAddress(rspec.IPv4Address("192.168.1.1", "255.255.255.0"))
cn_link = request.Link("cn-link-1")
cn_link.setNoBandwidthShaping()
cn_link.addInterface(cn_if)
good_cn_node.addService(rspec.Execute(shell="bash", command=OPEN5GS_DEPLOY_SCRIPT))

# single x310 for the good gNodeB
x310_node_pair(0, node_types[1][0], params.x310_good_radio, "Good gNodeB")

# 2x x310 reserved (in theory could be used for the first GNB)
x310_node_pair(2, node_types[0][0], params.x310_unused_radio_1, "Unused")
x310_node_pair(3, node_types[0][0], params.x310_unused_radio_2, "Unused")

# Evil GnB
evil_cn_node = request.RawPC("evilcn5g")
evil_cn_node.Site("Evil gNodeB")
#evil_cn_node.component_manager_id = COMP_MANAGER_ID
evil_cn_node.hardware_type = node_types[0][0]
evil_cn_node.disk_image = UBUNTU_IMG
cn_if = evil_cn_node.addInterface("cn-if")
cn_if.addAddress(rspec.IPv4Address("192.168.1.1", "255.255.255.0"))
cn_link = request.Link("cn-link-2")
cn_link.setNoBandwidthShaping()
cn_link.addInterface(cn_if)
evil_cn_node.addService(rspec.Execute(shell="bash", command=OPEN5GS_DEPLOY_SCRIPT))

# single x310 for the evil gNodeB
x310_node_pair(1, node_types[1][0], params.x310_evil_radio, "Evil gNodeB")



for ue_node_id, ue_name in indoor_ota_nucs:
    b210_nuc_pair(ue_node_id)

for frange in params.freq_ranges:
    request.requestSpectrum(frange.freq_min, frange.freq_max, 0)


tour = IG.Tour()
tour.Description(IG.Tour.MARKDOWN, tourDescription)
tour.Instructions(IG.Tour.MARKDOWN, tourInstructions)
request.addTour(tour)

pc.printRequestRSpec(request)
