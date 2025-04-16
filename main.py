# main.py
from wifi_doc_attack import wifi_deauth_attack
from bluetooth_doc_attack import bluetooth_attack
from syn_flood import syn_flood

def main():
    print("=== DoC-Attack Toolkit ===")
    print("1. Wi-Fi Deauth Attack")
    print("2. Bluetooth Flood Attack")
    print("3. SYN Flood (TCP)")
    choice = input("Select attack: ")

    if choice == '1':
        wifi_deauth_attack()
    elif choice == '2':
        bluetooth_attack()
    elif choice == '3':
        syn_flood()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
