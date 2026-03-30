import socket
from protocol.protocol import parse_message

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("[UDP SERVER STARTED]")

groups = {}          # group -> set of clients
client_group = {}    # client -> group

while True:
    data, addr = server.recvfrom(1024)
    msg = data.decode()

    msg_type, seq, group, content = parse_message(msg)

    # JOIN
    if msg_type == "JOIN":
        client_group[addr] = group

        if group not in groups:
            groups[group] = set()

        groups[group].add(addr)
        print(f"[JOIN] {addr} → {group}")

    # MESSAGE
    elif msg_type == "MSG":
        print(f"[MSG] {content}")

        # Send to all in same group
        for client in groups.get(group, []):
            if client != addr:
                server.sendto(data, client)

        # Send ACK
        ack = f"ACK|{seq}".encode()
        server.sendto(ack, addr)