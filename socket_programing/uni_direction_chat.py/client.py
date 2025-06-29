# CLIENT
import socket

c = socket.socket()
c.connect(("localhost", 9999))

name = input("Enter your name: ")
c.send(bytes(name, "utf-8"))

print(c.recv(1024).decode())

# Start chat loop
while True:
    msg = input("You: ")
    c.send(bytes(msg, "utf-8"))

    if msg.lower() == 'bye':
        print("You left the chat.")
        break

    reply = c.recv(1024).decode()
    print("Server:", reply)

c.close()
