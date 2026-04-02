import socket
import time
import threading
from protocol.protocol import create_msg, create_ack, create_join, parse_message

#  CHANGE THIS FOR MULTI-DEVICE
HOST = "127.0.0.1"   # Replace with server IP (e.g., "10.1.4.166")
PORT = 5000

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(2)   # timeout for ACK

# Join group
group = input("Enter group (A/B): ")
client.sendto(create_join(group).encode(), (HOST, PORT))

print(f"[CONNECTED] Joined group {group}")

# Sequence number
seq = 0

# Performance tracking
start_time = None
message_count = 0
TOTAL_MESSAGES = 5  


#  RECEIVE THREAD
def receive_messages():
    while True:
        try:
            data, _ = client.recvfrom(1024)
            msg = data.decode()

            mtype, seq_num, grp, content = parse_message(msg)

            if mtype == "MSG":
                print(f"\n[GROUP {grp}] {content}")

                # Send ACK back
                ack = create_ack(seq_num)
                client.sendto(ack.encode(), (HOST, PORT))

        except:
            pass


# SEND FUNCTION (WITH RETRANSMISSION)
def send_messages():
    global seq, start_time, message_count

    while True:
        msg = input("You: ")

        if not start_time:
            start_time = time.time()

        seq += 1
        packet = create_msg(seq, group, msg).encode()

        while True:
            client.sendto(packet, (HOST, PORT))

            try:
                data, _ = client.recvfrom(1024)
                mtype, ack_seq, _, _ = parse_message(data.decode())

                if mtype == "ACK" and ack_seq == seq:
                    print(f"[ACK RECEIVED for {seq}]")

                    message_count += 1

                    # Performance measurement
                    if message_count == TOTAL_MESSAGES:
                        end_time = time.time()
                        print(f"\n⏱ Time for {TOTAL_MESSAGES} messages: {end_time - start_time:.2f} sec")

                    break

            except socket.timeout:
                print("[RETRY] No ACK, resending...")


# Start receiver thread
threading.Thread(target=receive_messages, daemon=True).start()

# Start sending
send_messages()