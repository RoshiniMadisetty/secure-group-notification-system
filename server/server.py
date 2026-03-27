import socket
import ssl
import threading
import os
from protocol.protocol import parse_message

HOST = "0.0.0.0"
PORT = 5000

clients = []
lock = threading.Lock()

# 🔥 Group structures
groups = {}           # {group_name: [clients]}
client_group = {}     # {client: group}


# 🔁 Broadcast only within group
def broadcast_group(message, sender):
    group = client_group.get(sender)

    if not group:
        return

    for client in groups.get(group, []):
        if client != sender:
            try:
                client.send(message.encode())
            except:
                remove_client(client)


# ❌ Remove disconnected client
def remove_client(client):
    if client in clients:
        clients.remove(client)

    group = client_group.get(client)

    if group and client in groups.get(group, []):
        groups[group].remove(client)

    if client in client_group:
        del client_group[client]

    client.close()


# 👤 Handle each client
def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")

    while True:
        try:
            data = conn.recv(1024).decode()

            if not data:
                break

            msg_type, field, content = parse_message(data)

            # 🟢 JOIN GROUP
            if msg_type == "JOIN":
                group = field
                client_group[conn] = group

                if group not in groups:
                    groups[group] = []

                groups[group].append(conn)

                print(f"[JOIN] {addr} joined group {group}")

            # 🟡 MESSAGE
            elif msg_type == "MSG":
                print(f"[MESSAGE] {content}")
                broadcast_group(data, conn)

            # 🔵 ACK
            elif msg_type == "ACK":
                print(f"[ACK RECEIVED] message {field}")

        except:
            break

    print(f"[DISCONNECTED] {addr}")
    remove_client(conn)


# 🚀 Start server
def start_server():
    # 🔥 Fix certificate path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cert_path = os.path.join(base_dir, "security", "server.crt")
    key_path = os.path.join(base_dir, "security", "server.key")

    # 🔒 TLS setup
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert_path, keyfile=key_path)

    # 🌐 Socket setup
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    # 🔐 Wrap socket
    secure_socket = context.wrap_socket(server_socket, server_side=True)

    print("[SERVER STARTED]")
    print(f"Listening on {HOST}:{PORT}")

    while True:
        conn, addr = secure_socket.accept()

        with lock:
            clients.append(conn)

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start_server()