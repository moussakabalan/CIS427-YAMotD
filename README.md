# Socket Programming with YAMotD

This project demonstrates **client–server communication using Python sockets**.  
It uses a custom **"Yet Another Message of the Day" (YAMotD)** server that allows clients to retrieve or set a message of the day.

> ⚠️ **Note:** This version supports **only one client connection at a time**.

---

## 🛠️ Technologies Used
- **Language:** Python 3.x  
- **Libraries:** Built-in `socket` library  
- **Environment:** Developed using VS Code on Windows (compatible with any OS that supports Python)

---

## 📂 Project Structure
| File | Description |
|------|-------------|
| `Python/Server.py` | Starts the socket server, listens on a specified port, and handles incoming requests. |
| `Python/Client.py` | Connects to the server as a client, sends user input, and displays server responses. |

---

## 📦 Prerequisites
- Python 3.x installed  
- (Optional) CPython interpreter for your operating system  

---

## 🚀 How to Run

### 1. Start the Server
Open a terminal and run:
```bash
# (Windows)
py Python/Server.py
```
You should see:
```bash
Server is ready to receive requests on port 9400...
```
### 2. Start the Client
In a separate terminal:
```bash
# (Windows)
py Python/Client.py <server_ip>
```
> Use localhost as <server_ip> if running on the same device.
### 3. Available Commands
Once connected, the client supports the following commands:
```bash
MSGGET – Retrieve the current message of the day
MSGSTORE – Set a new message of the day
QUIT – Disconnect from the server
SHUTDOWN – Shut down the server (admin only)
```
---
## 📚 Networking Concepts Covered
- Creating TCP sockets
- Binding, listening, and accepting connections
- Sending and receiving messages
- Graceful connection termination

---

## 💡 Key Learnings
- Implemented a basic TCP client–server model
- Learned how to handle request/response loops over sockets
- Explored the limitations of single-client server design

---

## 🖼️ Demo

> <img width="606" height="122" alt="image" src="https://github.com/user-attachments/assets/20e78ac2-0b2f-4437-a488-ea296710a277" />

> <img width="749" height="288" alt="Screenshot 2025-09-04 at 6 21 30 PM" src="https://github.com/user-attachments/assets/6ac1989a-b790-4399-ad3f-7f69b9289f82" />

> <img width="746" height="174" alt="Screenshot 2025-09-04 at 6 22 43 PM" src="https://github.com/user-attachments/assets/b92139a4-51aa-46db-aea7-5895697c7af0" />

> <img width="763" height="181" alt="Screenshot 2025-09-04 at 6 22 58 PM" src="https://github.com/user-attachments/assets/59015243-1852-43cd-bb11-3ea2a29412f8" />

> <img width="825" height="286" alt="image" src="https://github.com/user-attachments/assets/b9dc0247-d5dd-4d60-bb09-7ec371fd4309" />

> <img width="779" height="151" alt="Screenshot 2025-09-04 at 6 24 07 PM" src="https://github.com/user-attachments/assets/710969df-a150-4212-ae59-22d238fde2b2" />

> <img width="819" height="166" alt="image" src="https://github.com/user-attachments/assets/4a91a635-5639-4406-bc62-1914c0772a45" />


*Original Project Dated 05/22/25*
