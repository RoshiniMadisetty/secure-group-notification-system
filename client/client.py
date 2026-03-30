import socket
import time
from protocol.protocol import create_msg, create_ack, create_join, parse_message

HOST = "127.0.0.1"   # change for multi-device
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(2)

group = input("Enter group (A/B): ")
client.sendto(create_join(group).encode(), (HOST, PORT))

seq = 0

def send_message():
    global seq

    while True:
        msg = input("You: ")
        seq += 1

        packet = create_msg(seq, group, msg).encode()

        # 🔁 RETRANSMISSION LOGIC
        while True:
            client.sendto(packet, (HOST, PORT))

            try:
                data, _ = client.recvfrom(1024)
                mtype, ack_seq, _, _ = parse_message(data.decode())

                if mtype == "ACK" and ack_seq == seq:
                    print(f"[ACK RECEIVED for {seq}]")
                    break

            except socket.timeout:
                print("[RETRY] No ACK, resending...")

def receive():
    while True:
        try:
            data, _ = client.recvfrom(1024)
            mtype, seq_num, grp, content = parse_message(data.decode())

            if mtype == "MSG":
                print(f"\n[GROUP {grp}] {content}")

                # Send ACK
                ack = create_ack(seq_num)
                client.sendto(ack.encode(), (HOST, PORT))

        except:
            pass


import threading
threading.Thread(target=receive, daemon=True).start()
send_message()