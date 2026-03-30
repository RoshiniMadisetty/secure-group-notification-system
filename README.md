<<<<<<< HEAD
# 🔐 Reliable UDP Group Notification System

## 📌 Overview

This project implements a **reliable UDP-based group notification system** that ensures message delivery using acknowledgments, retransmission, and timeout handling.
=======
# 🔐 Secure Reliable Group Notification System

## 📌 Overview

This project implements a **secure and reliable group notification system** using Python socket programming. It follows a **client–server architecture** where multiple clients communicate through a central server.

The system supports:

* Group-based messaging (A/B/C)
* Reliable delivery using ACK mechanism
* Secure communication using TLS
* Multi-client and multi-device support
>>>>>>> ec20caaecc05e8664622997dd9e118220a054b26

---

## 🚀 Features

<<<<<<< HEAD
* UDP-based communication
* Custom protocol with sequence numbers
* Group-based messaging
* Reliable delivery using ACK
* Timeout detection
* Automatic retransmission
* Multi-client support
=======
* Multi-client communication using TCP sockets
* Group-based notifications (no global broadcast)
* Custom protocol (`JOIN`, `MSG`, `ACK`)
* Reliable delivery with acknowledgments
* TLS-based encrypted communication
* Performance testing with simulated clients
>>>>>>> ec20caaecc05e8664622997dd9e118220a054b26

---

## 🏗️ Architecture

<<<<<<< HEAD
Clients join groups and communicate through a UDP server.

```text
Client → Server → Group Members
=======
```
Client A (Group A)     Client B (Group A)
        \                  /
         \                /
             --- SERVER ---
         /                \
Client C (Group B)     Client D (Group B)
```

* Clients join a group
* Server stores group mappings
* Messages are sent **only within the same group**

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
│   └── server.key   (NOT pushed to GitHub)
│
├── generate_cert.py
└── README.md
>>>>>>> ec20caaecc05e8664622997dd9e118220a054b26
```

---

<<<<<<< HEAD
## 📂 Structure

* `client/` → client code
* `server/` → UDP server
* `protocol/` → message format
* `performance/` → testing

---

## 🔒 Protocol

```text
JOIN|A
MSG|1|A|Hello
ACK|1
```

---

## ⚙️ Setup

```bash
git clone <repo>
=======
## 🔒 Protocol Design

Message formats:

```
JOIN|A
MSG|1|Hello
ACK|1
```

Flow:

```
Client joins group → sends message → server routes →
clients receive → send ACK
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/RoshiniMadisetty/secure-group-notification-system.git
>>>>>>> ec20caaecc05e8664622997dd9e118220a054b26
cd secure-group-notification-system
```

---

<<<<<<< HEAD
## ▶️ Run

### Server

```bash
python -m server.server
```

### Client

```bash
=======
### 2️⃣ Generate TLS Certificates (SERVER ONLY)

```
python generate_cert.py
```

This creates:

```
security/server.crt
security/server.key
```

---

## 🌐 Running on SAME SYSTEM

### Start Server

```
python -m server.server
```

### Start Clients

```
>>>>>>> ec20caaecc05e8664622997dd9e118220a054b26
python -m client.client
```

---

<<<<<<< HEAD
## 🌐 Multi-device Setup

* Server:
=======
## 🌍 Running on MULTIPLE SYSTEMS (IMPORTANT)

### 🖥️ Step 1: On SERVER Laptop

Edit `server/server.py`:

```
HOST = "0.0.0.0"
PORT = 5000
```

Run:

```
python -m server.server
```

Find server IP:

```
ipconfig
```

Example:

```
IPv4 Address: 10.45.5.6
```

---

### 💻 Step 2: On CLIENT Laptop

Edit `client/client.py`:

```
HOST = "10.45.5.6"
PORT = 5000
```

Run:

```
python -m client.client
```

---

### ⚠️ Requirements

* Both systems must be on the **same WiFi network**
* Allow Python through **Windows Firewall**
* Server must run **before clients**
>>>>>>> ec20caaecc05e8664622997dd9e118220a054b26

```python
HOST = "0.0.0.0"
```

<<<<<<< HEAD
* Client:

```python
HOST = "SERVER_IP"
```

---

## 🔁 Reliability Mechanism

* Each message has a sequence number
* Client waits for ACK
* If no ACK → retransmit
* Ensures reliable delivery over UDP

---

## 📊 Performance
=======
Simulates multiple clients connecting to server.

---

## 🔐 Security Notes

* TLS encryption ensures secure communication
* `server.key` is **private and not shared**
* Clients currently skip certificate verification for simplicity

---

## ⚠️ Limitations

* No authentication system
* Certificate verification disabled on client
* Works within same network (LAN)
>>>>>>> ec20caaecc05e8664622997dd9e118220a054b26

Supports multiple clients with concurrent communication.
---

<<<<<<< HEAD
## 📌 Conclusion

This project demonstrates how reliability can be implemented over UDP using sequence numbers, acknowledgments, and retransmission mechanisms.
=======

## 📌 Conclusion

This project demonstrates key networking concepts including **socket programming, secure communication, concurrency, and reliable group-based messaging**, making it a strong foundation for distributed systems.

---
>>>>>>> ec20caaecc05e8664622997dd9e118220a054b26
