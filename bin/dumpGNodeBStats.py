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