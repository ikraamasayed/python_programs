# SERVER
import socket

s = socket.socket()
print("Socket created...")

s.bind(('localhost', 9999))
s.listen(3)
print("Waiting for connection...")

c, addr = s.accept()
print("Connected with", addr)

name = c.recv(1024).decode()
print(f"{name} has joined the chat.")

c.send(bytes("Welcome to Sarvar Bhai Chat Room!", "utf-8"))

# Start chat loop
while True:
    msg = c.recv(1024).decode()
    if msg.lower() == 'bye':
        print(f"{name} left the chat.")
        c.send(bytes("bye", "utf-8"))
        break

    print(f"{name}: {msg}")
    reply = input("You: ")
    c.send(bytes(reply, "utf-8"))

c.close()
