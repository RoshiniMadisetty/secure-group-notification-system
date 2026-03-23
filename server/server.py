import socket
import ssl
import threading
from protocol.protocol import parse_message

HOST = "127.0.0.1"
PORT = 5000

clients = []
lock = threading.Lock()


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                remove_client(client)


def remove_client(client):
    if client in clients:
        clients.remove(client)
        client.close()


def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break

            msg_type, msg_id, content = parse_message(data)

            if msg_type == "MSG":
                print(f"[MESSAGE] {content}")
                broadcast(data, conn)

            elif msg_type == "ACK":
                print(f"[ACK RECEIVED] message {msg_id}")

        except:
            break

    print(f"[DISCONNECTED] {addr}")
    remove_client(conn)


def start_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("security/server.crt", "security/server.key")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    secure_socket = context.wrap_socket(server_socket, server_side=True)

    print("[SERVER STARTED]")
    print(f"Listening on {HOST}:{PORT}")

    while True:
        conn, addr = secure_socket.accept()

        with lock:
            clients.append(conn)

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


start_server()