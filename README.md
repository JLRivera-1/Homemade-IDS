# Homemade IDS

A simple Intrusion Detection System (IDS) designed to monitor and track devices on your local network. This project uses the ARP protocol to discover MAC addresses within a specified IP range, save those addresses in a text file, and alerts the user when no new devices are detected.

## Features
- Scans a local network range (e.g., 192.168.X.X/24) for active devices.
- Collects MAC addresses of devices on the network.
- Notifies the user when no new devices are found.
- Saves the discovered MAC addresses to a file for later reference.
  
***Designed for educational purposes and personal use on your own network.***

## Purpose
This project is intended for personal use and educational purposes. It’s a simple example of an IDS tool that can be used to monitor the devices on a local network. It’s useful for ensuring network security or tracking authorized devices within your home or small business network.

***Note: This tool should only be used on networks you own or have explicit permission to monitor.***

## How It Works
- ARP Requests: The script uses ARP requests to discover devices on the local network. It broadcasts a request to the IP range you specify (default: 192.168.1.0/24).
- Collect MAC Addresses: Each device on the network responds with its MAC address, which is then collected and saved to the macAddresses file.
- Notification: The tool checks for new MAC addresses. If no new devices are detected, it notifies you and stops.

## Installation
To use this project, simply upload the code files to your local machine or server. There are no special installation requirements beyond having the necessary Python libraries installed.

## Requirements
- Python 3.x
- Scapy: A powerful Python library used for network packet manipulation.
- Plyer: A library for cross-platform notifications.

## Usage
- Clone or download this repository to your local machine.
- Open a terminal and navigate to the directory containing the homemade IDS.py script.
- Run the script:
  python homemade IDS.py
The script will continuously monitor the network and gather MAC addresses of devices within the specified IP range. If no new devices are found, it will notify you and stop.

### Customizing the Network Range
You can customize the network range by editing the script or passing a different IP range when calling the get_mac_addresses function.
- Example:
  mac_Addresses = get_mac_addresses("192.168.0.0/24") # Replace with your network range
