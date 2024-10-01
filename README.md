# CS6480-Final-Project
CS6480-Final-Project

Project Members

* Mumtahin Mazumder
* Mike Tomer






# Idea

From the original idea pitch

>Impact of miss-aligned 5G frame structures in supporting diverse applications

Current 5G systems are typically optimized for downlink traffic. I.e.,for providing mobile broadband services to end users, who are typically *downloading* more content than they are uploading.

Emerging 5G applications/services might require a change in that. E.g., remote driving involves significant uplink traffic (i.e., in the form of video and other sensor data used to inform the remote driver), and also requires relatively low latency to ensure the remote driver can take timely actions.

This project will (start to) evaluate the impact of miss-aligned 5G frame structures on adjacent service providers. E.g.,  where one provider is providing downlink heavy (e.g., mobile broadband) services, while a neighbor is providing uplink heavy (e.g., tele-operated driving) services.

A possible starting point would be to instantiate two differently configured 5G networks in adjacent bands in POWDER and to evaluate the impact.




# Plans for implementation





# Experiments to run

* Have a neighboring high use channel uploading and a channel downloading.
* high upload on both sides of a downloading channel.


# Things to figure out

* how to instantiate real (not simulated) networks in powder
* How to chose the bands
* Figure out how close we can get them (can we overlap)?