import socket
import threading
from dotenv import load_dotenv
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
            index = client.index(client)
            clients.remove(index)
            client.close()
            nickname = nicknames[index]
            print(f'{nickname} has left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive_connection():
    while True:
        print(f'starting up server PORT:{Config.PORT} and HOST:{Config.HOST}')
        client , address = server.accept()
        print(f'Connected with address {address}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('connected to server'.encode('ascii'))

        thread = threading.Thread( target = handle_clients, args = client )
        thread.start()


receive_connection()