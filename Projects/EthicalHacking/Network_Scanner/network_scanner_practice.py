#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst = ip) # instance of an ARP packet object
    # arp_request.pdst = ip
    print(arp_request.summary())
    # scapy.ls(scapy.ARP()) # get list of fields for a particular class
    broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff') # The boradcast MAC address is a "virtual MAC address" -  it does not exist in reality
    # broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    scapy.ls(scapy.Ether())

    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()
    answered, unanswered = scapy.srp(arp_request_broadcast) # using srp rather tahn sr due to the custom Ether portion of the packet
    # answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout = 1)
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1)[0]

    answered_list = scapy.srp(arp_request_broadcast, timeout= 1, verbose= False)[0]
    for element in answered_list:
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("----------------------------------------------------")
        # print(element[1].show())

scan("10.20.14.1/24")

