import socket
import threading
from config import Config

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((Config.HOST,Config.PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle_clients(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            print(f'{nickname} has left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive_connection():
    while True:
        print(f'starting up server PORT:{Config.PORT} and HOST:{Config.HOST}')
        client , address = server.accept()
        print(f'Connected with address {address}')

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat'.encode('utf-8'))
        client.send(f'{nickname} welcome to the chat'.encode('utf-8'))

        thread = threading.Thread( target = handle_clients, args = (client,) )
        thread.start()


receive_connection()