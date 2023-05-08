#!/usr/bin/env python

import subprocess
import optparse
import re

mac_regex = r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w"

# todo include an argument so the user can display available interfaces
# todo include an error handling if the specified interface does not exist


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface_card", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface_card:
        parser.error("[-] Please specify an interface, use --help for more info.")
    if not options.new_mac:
        parser.error("[-] Please specify an new MAC, use --help for more info.")
    return options


def change_mac(interface_card, new_mac):
    information = "[+] Changing MAC address for: {} to: {}".format(interface_card, new_mac)
    print(information)
    subprocess.call(["ifconfig", interface_card, "down"])
    subprocess.call(["ifconfig", interface_card, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface_card, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(mac_regex, str(ifconfig_result))

    if mac_address_search_result:
        # print(mac_address_search_result.group(0))
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address on the specified interface.")


user_input = get_arguments()

current_mac = get_current_mac(user_input.interface_card)
print("current MAC: " + str(current_mac))

change_mac(user_input.interface_card, user_input.new_mac)

current_mac = get_current_mac(user_input.interface_card)

if current_mac == user_input.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")


