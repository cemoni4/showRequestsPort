#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
from collections import defaultdict

request_count = defaultdict(int)

def inject_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.TCP):
    
        if scapy_packet[scapy.TCP].dport in range(21, 444):
            ip_src = scapy_packet[scapy.IP].src
            port_dst = scapy_packet[scapy.TCP].dport

            request_count[(ip_src, port_dst)] += 1
            print(f"[+] {ip_src}:{port_dst} - {request_count[(ip_src, port_dst)]} richieste")

        elif scapy_packet[scapy.TCP].sport in range(21, 444):
            ip_dst = scapy_packet[scapy.IP].dst
            port_src = scapy_packet[scapy.TCP].sport

            request_count[(ip_dst, port_src)] += 1
            print(f"[+] {ip_dst}:{port_src} - {request_count[(ip_dst, port_src)]} richieste")
    else:
        print("[!] Pacchetto non TCP, ignorato.")
    
    packet.accept()

packet_queue = netfilterqueue.NetfilterQueue()
packet_queue.bind(1, inject_packet) 
packet_queue.run() 
