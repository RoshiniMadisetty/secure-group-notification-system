import socket
import time

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

group = "A"
client.sendto(f"JOIN|{group}".encode(), (HOST, PORT))

start = time.time()

for i in range(5):
    msg = f"MSG|{i}|{group}|fast test"
    client.sendto(msg.encode(), (HOST, PORT))
    print(f"Sent {i}")

end = time.time()

print(f"\nFAST UDP Time: {end - start:.6f} seconds")