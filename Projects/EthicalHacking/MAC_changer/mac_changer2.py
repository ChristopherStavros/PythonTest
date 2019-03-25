#!/usr/bin/env python3

import subprocess
import optparse

parser = optparse.OptionParser()

interface =  raw_input("interface > ")
new_mac = raw_input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac) #08:00:27:95:8c:5e

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
