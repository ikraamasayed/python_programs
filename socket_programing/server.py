import socket

s = socket.socket()     #create a socket (ipv4/ipv6 , type of protocol)
print("socket created...")

s.bind(('localhost',9999)) #bind socket with (port no & ip) *bind takes 1 arg* 

s.listen(3)    #no of connection 
print("waiting for connection...")

while True:     # using loop for accepting request for more than 1 connection 
    c,addr = s.accept()  
    name = c.recv(1024).decode()
    print("connected with ",addr,name)


    c.send(bytes("Welcome to Sarvar Bhai ","utf-8"))     #works on byte format & utf-8 encode
    c.close()