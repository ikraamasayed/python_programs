#simple TCP chat room in python 

import socket
import threading

host = "localhost"
port = 5050

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

nicknames = []
clients = []

def broadcast(message):
    for  client in clients :
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast(f'{nickname}left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:

        client,address = server.accept()
        print(f'Connect to {str(address)}')

        client.send(f'Nick'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nicknames)
        clients.append(client)

        print(f'Nickname of client is {nickname}')
        broadcast(f'{nickname} Joined the chat '.encode('ascii'))
        client.send("Connected to the server".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("server is listening")
receive()
