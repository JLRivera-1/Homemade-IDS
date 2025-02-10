from scapy.all import ARP, Ether, srp, sniff
from plyer import notification

def get_mac_addresses(target_ip):
    # List to store MAC addresses
    mac_Addresses = []

    # Create Ethernet and ARP request packets using Scapy
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address
    arp = ARP(pdst=target_ip)  # ARP request for target IP
    packet = ether/arp  # Combine both packets

    # Send the packet and receive responses using Scapy's SRP (Send/Receive Protocol)
    full_packet = srp(packet, timeout=30, verbose=False)[0]
    for sent, received in full_packet:
        mac_Addresses.append(received.hwsrc)

    return mac_Addresses

# Continuously gather MAC addresses until no new ones are found
while True:
    mac_Addresses = get_mac_addresses("192.168.x.x/24")

    with open('macAddresses', 'a+') as file:
        file.seek(0)
        file_lines = file.readlines()
        new_macs_found = False
        for mac in mac_Addresses:
            if mac + "\n" not in file_lines:
                file.write(mac + "\n")
                new_macs_found = True
        
        if not new_macs_found:
            print("No new MAC Addresses found in IP range.")  # Print to terminal when done
            notification.notify(
                title='Homemade IDS',
                message='No new MAC addresses found.',
                timeout=10  # Notify user after completion
            )
            break
