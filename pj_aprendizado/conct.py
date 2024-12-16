import socket
import ipaddress

def get_local_network():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    network = ipaddress.ip_network(f"{local_ip}/24", strict=False)
    return local_ip, network

local_ip, network = get_local_network()
print(f"IP Local: {local_ip}")
print(f"Rede: {network}")
