#!/usr/bin/env python3

import subprocess
import optparse


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


user_input = get_arguments()
change_mac(user_input.interface_card, user_input.new_mac)

