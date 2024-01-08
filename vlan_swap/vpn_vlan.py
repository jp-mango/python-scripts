import subprocess
import sys


def set_ip(interface_name, ip, subnet_mask, gateway):
    # Set the IP address
    subprocess.call(
        f'netsh interface ip set address name="{interface_name}" static {ip} {subnet_mask} {gateway}'
    )

    # Print the new configuration
    print(f"IP set to {ip} on {interface_name}")


def main():
    vlan = input("Enter VLAN (mgmt/vpn): ").lower()

    # set interface name
    interface_name = "Ethernet 2"

    if vlan == "mgmt":
        # Set IP for management VLAN
        set_ip(interface_name, "192.168.10.14", "255.255.255.0", "192.168.10.1")
    elif vlan == "vpn":
        # Set IP for VPN VLAN
        set_ip(interface_name, "192.168.70.14", "255.255.255.0", "192.168.70.1")
    else:
        print("Invalid VLAN. Please enter 'mgmt' or 'vpn'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
