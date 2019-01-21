import subprocess

variables ={
    "interface" : "eth0",
    "new_mac" : "00:11:22:33:44:67"
}

print("[+] Changing MAC address for {interface} to {new_mac}".format(**variables))

subprocess.call("ifconfig {interface} down".format(**variables), shell=True)
subprocess.call("ifconfig {interface} hw ether {new_mac}".format(**variables), shell=True)
subprocess.call("ifconfig {interface} up".format(**variables), shell=True)

