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
- Up to four NUC compute nodes, each with a COTS 5G module and supporting tools

Note: This profile currently defaults to using the 3430-3470 MHz spectrum range and you need an approved reservation for this spectrum in order to use it. It's also strongly recommended that you include the following necessary resources in your reservation to gaurantee their availability at the time of your experiment:

- A d430 compute node to host the core network
- A d740 compute node for the spectrum observation node
- At least one indoor OTA NUCs with COTS UEs

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

tourInstructions = "Loading from file"
with open(f'{os.path.dirname(os.path.abspath(__file__))}/README.md', 'r') as file:
    data = file.read()


tour = IG.Tour()
tour.Description(IG.Tour.MARKDOWN, tourDescription)
tour.Instructions(IG.Tour.MARKDOWN, tourInstructions)
request.addTour(tour)

pc.printRequestRSpec(request)
