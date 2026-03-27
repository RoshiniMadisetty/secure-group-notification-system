# 🔐 Secure Reliable Group Notification System

## 📌 Overview

This project implements a **secure and reliable group notification system** using Python socket programming. It follows a **client–server architecture** where multiple clients communicate through a central server.

The system supports:

* Group-based messaging (A/B/C)
* Reliable delivery using ACK mechanism
* Secure communication using TLS
* Multi-client and multi-device support

---

## 🚀 Features

* Multi-client communication using TCP sockets
* Group-based notifications (no global broadcast)
* Custom protocol (`JOIN`, `MSG`, `ACK`)
* Reliable delivery with acknowledgments
* TLS-based encrypted communication
* Performance testing with simulated clients

---

## 🏗️ Architecture

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
```

---

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
cd secure-group-notification-system
```

---

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
python -m client.client
```

---

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

---

## 📊 Performance Testing

Run:

```
python -m performance.test_clients
```

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

---


## 📌 Conclusion

This project demonstrates key networking concepts including **socket programming, secure communication, concurrency, and reliable group-based messaging**, making it a strong foundation for distributed systems.

---
