import socket
import ssl
import threading
import time

HOST = "10.14.166"
PORT = 5000
NUM_CLIENTS = 10   # change this to increase clients

def create_client(client_id):
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        raw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s = context.wrap_socket(raw, server_hostname="localhost")

        s.connect((HOST, PORT))

        message = f"MSG|{client_id}|Hello from client {client_id}"
        s.send(message.encode())

        print(f"[CONNECTED] Client {client_id}")

        time.sleep(1)

        s.close()

    except Exception as e:
        print(f"[ERROR] Client {client_id}:", e)


threads = []

for i in range(NUM_CLIENTS):
    t = threading.Thread(target=create_client, args=(i,))
    t.start()
    threads.append(t)

    time.sleep(0.2)   # 🔥 IMPORTANT (prevents crash)


for t in threads:
    t.join()

print(f"\n✅ {NUM_CLIENTS} clients completed successfully")