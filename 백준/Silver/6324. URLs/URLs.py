import sys

input = sys.stdin.readline
n = int(input().rstrip())

for i in range(1, n + 1):
    s = input().rstrip()

    protocol, _, rest = s.partition("://")
    
    host_port, _, path_part = rest.partition("/")
    host, _, port_part = host_port.partition(":")

    port = port_part if port_part else "<default>"
    path = path_part if path_part else "<default>"

    print(f"URL #{i}")
    print(f"Protocol = {protocol}")
    print(f"Host     = {host}")
    print(f"Port     = {port}")
    print(f"Path     = {path}")
    print()