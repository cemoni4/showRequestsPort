# Packet Monitoring Tool 🛡️

## Description 📘
This project is a Python script that uses `netfilterqueue` and `scapy` to intercept and monitor TCP traffic on specific ports. Each intercepted packet is analyzed, and the script keeps track of the number of requests made by each IP to certain ports.

## Features ⚡
- **TCP Packet Interception**: Captures TCP packets using a Netfilter queue.
- **Request Counting by IP and Port**: Tracks how many requests are made to and from each IP-port combination.
- **Real-Time Output**: Prints the request count live in the console.

## Requirements 🛠️
- Python 3
- Libraries:
  - `netfilterqueue`
  - `scapy`

Install the required libraries with:
```bash
pip install netfilterqueue scapy
```

## Firewall Configuration 🔥
To make the script work, you need to set up an iptables rule to forward traffic to the Netfilter queue:
```bash
iptables -I FORWARD -j NFQUEUE --queue-num 1
```

For local testing:
```bash
iptables -I OUTPUT -j NFQUEUE --queue-num 1
iptables -I INPUT -j NFQUEUE --queue-num 1
```

After running the script, you can reset the rules with:
```bash
iptables --flush
```

## Execution ▶️
Run the script with:
```bash
sudo python3 monitor.py
```

## Warning ⚠️
Running this script requires superuser privileges and modifies firewall rules. Use responsibly and only in controlled environments!

## License 📄
Distributed under the MIT License.

---



