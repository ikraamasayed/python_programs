import socket

c = socket.socket()

c.connect(("localhost",9999))       #connect with server 

name = input("enter client's name ")
c.send(bytes(name,"utf-8"))

print(c.recv(1024).decode())        #recieve from the server with buffer size 1024 & decode 