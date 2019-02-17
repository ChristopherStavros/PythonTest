#!/usr/bin/env python

import subprocess

interface =  input("interface > ")
new_mac = input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac) #08:00:27:95:8c:5e

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


###LESS SECURE -- HACKABLE

# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up ", shell=True)

# variables = {
#     "interface" : input("interface > "), #eth0",  wlan0
#     "new_mac" : input("new MAC > ") #00:11:22:33:44:67"   5c:51:4f:28:49:d9
# }

###COOLER VERSION, but still NOT SECURE -- HACKABLE

# print("[+] Changing MAC address for {interface} to {new_mac}".format(**variables))

# subprocess.call("ifconfig {interface} down".format(**variables), shell=True)
# subprocess.call("ifconfig {interface} hw ether {new_mac}".format(**variables), shell=True)
# subprocess.call("ifconfig {interface} up".format(**variables), shell=True)


