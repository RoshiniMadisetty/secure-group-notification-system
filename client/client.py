import socket
import ssl
import threading
from protocol.protocol import format_message, format_ack, parse_message

HOST = "127.0.0.1"
PORT = 5000

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = context.wrap_socket(raw_socket, server_hostname="localhost")

client.connect((HOST, PORT))

msg_id = 1


def receive_messages():
    while True:
        try:
            data = client.recv(1024).decode()

            if not data:
                break

            msg_type, received_id, content = parse_message(data)

            if msg_type == "MSG":
                print(f"\nNotification: {content}")

                ack = format_ack(received_id)
                client.send(ack.encode())

        except:
            break


thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()

while True:
    message = input("Enter message: ")
    formatted = format_message(msg_id, message)
    client.send(formatted.encode())
    msg_id += 1