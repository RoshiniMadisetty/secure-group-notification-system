# 🔐 Reliable UDP Group Notification System

## 📌 Overview

This project implements a **reliable UDP-based group notification system** that ensures message delivery using acknowledgments, retransmission, and timeout handling.

---

## 🚀 Features

* UDP-based communication
* Custom protocol with sequence numbers
* Group-based messaging
* Reliable delivery using ACK
* Timeout detection
* Automatic retransmission
* Multi-client support

---

## 🏗️ Architecture

Clients join groups and communicate through a UDP server.

```text
Client → Server → Group Members
```

---

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
cd secure-group-notification-system
```

---

## ▶️ Run

### Server

```bash
python -m server.server
```

### Client

```bash
python -m client.client
```

---

## 🌐 Multi-device Setup

* Server:

```python
HOST = "0.0.0.0"
```

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

Supports multiple clients with concurrent communication.
---

## 📌 Conclusion

This project demonstrates how reliability can be implemented over UDP using sequence numbers, acknowledgments, and retransmission mechanisms.
