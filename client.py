import socket
import threading
from config import Config

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect( (Config.HOST,Config.PORT) )

nickname = input("choose a nickname :")

def connect_server():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(f'{message} from server received')

        except Exception as error:
            print(f'an error ocurred {error}')
            client.close()
            break