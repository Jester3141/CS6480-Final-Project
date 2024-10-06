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

before starting the gNB, edited /etc/srsran/gnb.cfg and chagned the addr in the metric session to local host.

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
        for entry in received_data:
            json.dump(entry, file)
            file.write("\n")  # Add a new line after each entry
    print(f"Received data saved to {filename}. Exiting...")
```

Started this script.

Then started the GNB


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


Received JSON: {'timestamp': 1728188249.32, 'ue_list': [{'ue_container': {'pci': 1, 'rnti': 17921, 'cqi': 15, 'ri': 1, 'dl_mcs': 21, 'dl_brate': 10120.0, 'dl_nof_ok': 13, 'dl_nof_nok': 3, 'dl_bs': 3, 'pusch_snr_db': 65.532005, 'ul_mcs': 26, 'ul_brate': 28000.0, 'ul_nof_ok': 14, 'ul_nof_nok': 0, 'bsr': 53}}]}
Received JSON: {'timestamp': 1728188250.433, 'rlc_metrics': [{'drb': {'du_id': 0, 'ue_id': 0, 'drb_id': 1, 'tx': {'num_sdus': 0, 'num_sdu_bytes': 0, 'num_dropped_sdus': 0, 'num_discarded_sdus': 0, 'num_discard_failures': 0, 'num_pdus': 0, 'num_pdu_bytes': 0}, 'rx': {'num_sdus': 0, 'num_sdu_bytes': 0, 'num_pdus': 0, 'num_pdu_bytes': 0, 'num_lost_pdus': 0, 'num_malformed_pdus': 0}}}]}



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






