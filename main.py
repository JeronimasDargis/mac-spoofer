#!/usr/bin/env python3

import subprocess

interfaceCard = input("interface > ")
newMac = input("new MAC > ")

information = "[+] Changing MAC address for: {} to: {}".format(interfaceCard, newMac)

print(information)

# subprocess.call("ifconfig " + interfaceCard + " down", shell=True)
# subprocess.call("ifconfig " + interfaceCard + " hw ether " + newMac, shell=True)
# subprocess.call("ifconfig " + interfaceCard + " up", shell=True)