# showRequestsPort
Show Requests Port is a simple Python-based port scanner that allows you to quickly check which ports on a target host are open and responding to requests.

🔥 TCP Request Monitor
This Python script monitors TCP traffic and counts the number of requests per IP and port. It works by intercepting packets using NetfilterQueue and Scapy.

📌 Features
✅ Monitors TCP traffic on ports 21-443
✅ Keeps track of request counts for each IP-port combination
✅ Works with iptables to capture packets
✅ Prints real-time request statistics

⚙️ Installation
Make sure you have Python 3 installed and install the required dependencies:

bash
Copia
Modifica
pip install netfilterqueue scapy
You also need to configure iptables to forward packets to the NetfilterQueue.

bash
Copia
Modifica
sudo iptables -I FORWARD -j NFQUEUE --queue-num 1
(Use INPUT instead of FORWARD if running locally.)

🚀 Usage
1️⃣ Run the script with root privileges:

bash
Copia
Modifica
sudo python3 monitor.py
2️⃣ The script will start monitoring TCP traffic and print logs like this:

less
Copia
Modifica
[+] 192.168.1.10:80 - 5 requests
[+] 192.168.1.20:443 - 2 requests
3️⃣ When done, reset your iptables rule:

bash
Copia
Modifica
sudo iptables -D FORWARD -j NFQUEUE --queue-num 1
📂 Creating an IP List (iplist)
If you want to filter specific IPs, you can create an iplist.txt file with one IP per line:

Copia
Modifica
192.168.1.10
192.168.1.20
Modify the script to only track requests from these IPs:

python
Copia
Modifica
with open("iplist.txt", "r") as file:
    ip_list = set(file.read().splitlines())

if ip_src in ip_list:
    request_count[(ip_src, port_dst)] += 1
⚠️ Disclaimer
This tool is for educational purposes only. Use it responsibly and only on networks you own or have permission to monitor. 🛑

📜 License
Distributed under the MIT License.


