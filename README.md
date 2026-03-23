# secure-group-notification-system
# 🔐 Secure Reliable Group Notification System

## 📌 Overview

This project implements a **secure and reliable group notification system** using low-level socket programming in Python. It follows a **client–server architecture** where a central server manages communication between multiple clients.

The system ensures:

* Reliable message delivery using **ACK-based protocol**
* Secure communication using **TLS (SSL encryption)**
* Support for **multiple concurrent clients**

---

## 🚀 Features

* Multi-client communication using TCP sockets
* Custom message protocol (`MSG`, `ACK`, Message IDs)
* Reliable delivery with acknowledgment tracking
* TLS-based secure communication
* Performance testing with simulated clients
* Packet analysis using Wireshark

---

## 🏗️ Architecture

```
Client A       Client B       Client C
    \             |             /
     \            |            /
          --------SERVER--------
                 |
          Message Broadcast
```

* Clients connect to the server using TCP sockets
* Server broadcasts messages to all connected clients
* Clients send ACKs to confirm delivery

---

## 📂 Project Structure

```
secure-group-notification-system
│
├── client/
│   └── client.py
│
├── server/
│   └── server.py
│
├── protocol/
│   └── protocol.py
│
├── performance/
│   └── test_clients.py
│
├── security/
│   ├── server.crt
│   └── server.key
│
├── docs/
└── README.md
```

---

## ⚙️ Technologies Used

* Python (Socket Programming)
* TCP/IP Networking
* SSL/TLS Encryption
* Threading (Concurrency)
* Wireshark (Network Analysis)

---

## 🔒 Protocol Design

Message format:

```
MSG|<message_id>|<message>
```

Acknowledgment:

```
ACK|<message_id>
```

Example:

```
MSG|1|Hello team
ACK|1
```

---

## 🛠️ Setup & Installation

### 1. Clone the Repository

```
git clone https://github.com/your-username/secure-group-notification-system.git
cd secure-group-notification-system
```

---

### 2. Generate TLS Certificate

Run:

```
openssl req -new -x509 -days 365 -nodes -out security/server.crt -keyout security/server.key
```

Press Enter for all prompts.

---

## ▶️ How to Run

### Step 1: Start Server

```
python -m server.server
```

---

### Step 2: Start Clients (Open multiple terminals)

```
python -m client.client
```

---

### Step 3: Send Messages

Type messages in any client terminal.
Other clients will receive notifications.

---

## 📊 Performance Testing

Run:

```
python -m performance.test_clients
```

This simulates multiple clients connecting to the server.

---

## 📡 Network Analysis

Network communication was analyzed using Wireshark to verify:

* TCP packet exchange
* Message transmission
* TLS encryption (encrypted payload visibility)

---

## 📈 Evaluation Metrics

* Latency (response time)
* Throughput (messages/sec)
* Scalability (number of clients handled)

---



## 📌 Conclusion

This project demonstrates key networking concepts including **socket programming, secure communication, concurrency, and reliable data transfer**, making it a strong foundation for distributed systems and backend development.

---
