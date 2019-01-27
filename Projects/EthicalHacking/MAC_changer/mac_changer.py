#!/usr/bin/env python3

import subprocess

variables ={
    "interface" : input("interface > "), #eth0",  wlan0
    "new_mac" : input("new MAC > ") #00:11:22:33:44:67"   5c:51:4f:28:49:d9
}

print("[+] Changing MAC address for {interface} to {new_mac}".format(**variables))

subprocess.call("ifconfig {interface} down".format(**variables), shell=True)
subprocess.call("ifconfig {interface} hw ether {new_mac}".format(**variables), shell=True)
subprocess.call("ifconfig {interface} up".format(**variables), shell=True)

