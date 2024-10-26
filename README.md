# CS6480-Final-Project
CS6480-Final-Project

Project Members

* Mumtahin Mazumder
* Mike Tomer



# Project overleaf link

https://www.overleaf.com/project/66fb5c7f570d812e548bfae0



# Idea

From the original idea pitch

>Impact of miss-aligned 5G frame structures in supporting diverse applications

Current 5G systems are typically optimized for downlink traffic. I.e.,for providing mobile broadband services to end users, who are typically *downloading* more content than they are uploading.

Emerging 5G applications/services might require a change in that. E.g., remote driving involves significant uplink traffic (i.e., in the form of video and other sensor data used to inform the remote driver), and also requires relatively low latency to ensure the remote driver can take timely actions.

This project will (start to) evaluate the impact of miss-aligned 5G frame structures on adjacent service providers. E.g.,  where one provider is providing downlink heavy (e.g., mobile broadband) services, while a neighbor is providing uplink heavy (e.g., tele-operated driving) services.

A possible starting point would be to instantiate two differently configured 5G networks in adjacent bands in POWDER and to evaluate the impact.




# Plans for implementation

Dustin Moss 5G expert


# Project flow (according to professor)

We have off the shelf UEs and RUs.  

tddsystem,  downlink and uplink share


# Experiments to run

* Have a neighboring high use channel uploading and a channel downloading.
* high upload on both sides of a downloading channel.


# Things to figure out

* how to instantiate real (not simulated) networks in powder
* How to chose the bands
* Figure out how close we can get them (can we overlap)?






# getting metrics


Started everything like in lab on simulated hardware.

before starting the gNB, edited /etc/srsran/gnb.cfg and chagned the addr in the metric session to local host
with the following command
```shell
sudo sed -i 's/addr: 172.19.1.4/addr: 127.0.0.1/g' /etc/srsran/gnb.conf
```

https://docs.srsran.com/projects/project/en/latest/user_manuals/source/outputs.html#json-metrics




```python
import socket
import json

UDP_IP = "127.0.0.1"   # IP address to bind to (localhost in this case)
UDP_PORT = 55555       # Port to bind to

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
    filename = "gnb_metrics.json"
    with open(filename, "w") as file:
        json.dump(received_data, file)
    print(f"Received data saved to {filename}. Exiting...")
```

Started this script.

Then started the GNB


The items received by the stats are described here:

https://docs.srsran.com/projects/project/en/latest/user_manuals/source/console_ref.html#manual-console-ref

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

Items that are in the JSON are also described below.

Here are the items not in the JSON.

pusch:  PUSCH SINR (Signal-to-Interference-plus-Noise Ratio)
rsrp:   Reference Signal Received Power   https://www.sharetechnote.com/html/5G/5G_PowerDefinition.html
ta:     Timing Advance in microseconds    https://www.sharetechnote.com/html/5G/5G_TimingAdvance.html
phr:    Power Headroom as reported by the UE  https://www.sharetechnote.com/html/Handbook_LTE_PHR.html

{
  "timestamp": 1700671417.005,
  "ue_list": [
    {
      "ue_container": {
        "pci": 1,  # Physical Cell Identifier  https://www.sharetechnote.com/html/Handbook_LTE_PCI.html
        "rnti": 17921,  # Radio Network Temporary Identifier (UE identifier)   https://www.sharetechnote.com/html/5G/5G_RNTI.html
        "cqi": 15, # Channel Quality Indicator reported by the UE (1-15)   https://www.sharetechnote.com/html/Handbook_LTE_CQI.html
        "ri": 1,    # Rank Indicator as reported by the UE   https://www.sharetechnote.com/html/Handbook_LTE_RI.html
        "dl_mcs": 27,  # Modulation and Coding Scheme (0-28)      QAM type and Coding rate  https://www.sharetechnote.com/html/5G/5G_MCS_TBS_CodeRate.html
        "dl_brate": 291680.0,  # Bitrate (bits/sec)
        "dl_nof_ok": 352,   # Number of packets successfully sent
        "dl_nof_nok": 0,    # Number of packets dropped
        "dl_bs": 0,   # Downlink Buffer Status, data waiting to be transmitted as reported by the gNB (bytes)
        "pusch_snr_db": 24.025097,  # Uplink SNR.
        "ul_mcs": 26,  # Modulation and Coding Scheme (0-28)      QAM type and Coding rate  https://www.sharetechnote.com/html/5G/5G_MCS_TBS_CodeRate.html
        "ul_brate": 12838928.0,  # Bitrate (bits/sec)
        "ul_nof_ok": 431,  # Number of packets successfully sent
        "ul_nof_nok": 0,# Number of packets dropped
        "bsr": 0  # Buffer Status Report, data waiting to be transmitted as reported by the UE (bytes)  https://www.sharetechnote.com/html/Handbook_LTE_BSR.html
      }
    }
  ]
}

Received JSON: {'timestamp': 1728188249.32, 'ue_list': [{'ue_container': {'pci': 1, 'rnti': 17921, 'cqi': 15, 'ri': 1, 'dl_mcs': 21, 'dl_brate': 10120.0, 'dl_nof_ok': 13, 'dl_nof_nok': 3, 'dl_bs': 3, 'pusch_snr_db': 65.532005, 'ul_mcs': 26, 'ul_brate': 28000.0, 'ul_nof_ok': 14, 'ul_nof_nok': 0, 'bsr': 53}}]}
Received JSON: {'timestamp': 1728188250.433, 'rlc_metrics': [{'drb': {'du_id': 0, 'ue_id': 0, 'drb_id': 1, 'tx': {'num_sdus': 0, 'num_sdu_bytes': 0, 'num_dropped_sdus': 0, 'num_discarded_sdus': 0, 'num_discard_failures': 0, 'num_pdus': 0, 'num_pdu_bytes': 0}, 'rx': {'num_sdus': 0, 'num_sdu_bytes': 0, 'num_pdus': 0, 'num_pdu_bytes': 0, 'num_lost_pdus': 0, 'num_malformed_pdus': 0}}}]}


Which profile? srs-indoor-ota

tdd (Time division Duplexing) parameterization?



Will instantiate 1 normal setup gNBs core with 1 or more UEs connected to the first gNB where measurements will be recorded.  Iperf will be ran on this one with the UEs connected here.

Additionally we will have 1 more gNB in test mode where it is in test mode and constantly transmitting.  This second one allows
us to configure the interference more easily.

UE1-4  ------------ > GNB -> Core

                      Evil GNB


how to get UE metrics?
And IperfD

Knobs GnB are transmit power and the tdd config.  https://gitlab.flux.utah.edu/dmaas/srs-indoor-ota/-/blob/master/etc/srsran/gnb_rf_x310_tdd_n78_40mhz.yml?ref_type=heads


Need to figure out how to run the EVIL gNB.  Some kind of a boolean flag.  Read the documentation....

