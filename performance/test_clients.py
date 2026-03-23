import socket
import ssl
import threading
import time

HOST = "127.0.0.1"
PORT = 5000

def create_client(i):
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        raw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s = context.wrap_socket(raw, server_hostname="localhost")

        s.connect((HOST, PORT))
        s.send(f"MSG|{i}|performance test".encode())

        print(f"Client {i} connected")

        time.sleep(1)
        s.close()

    except Exception as e:
        print(f"Client {i} error:", e)


threads = []

for i in range(20):
    t = threading.Thread(target=create_client, args=(i,))
    t.start()
    threads.append(t)
    time.sleep(0.1)   # prevents overload


for t in threads:
    t.join()

print("Performance test completed - 20 clients simulated")