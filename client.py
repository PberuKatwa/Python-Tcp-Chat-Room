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
                print(f'{message}')

        except Exception as error:
            print(f'an error ocurred {error}')
            client.close()
            break

def write_message():
    while True:
        message = f'{nickname}: { input("") }'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=connect_server)
receive_thread.start()

write_thread = threading.Thread(target=write_message)
write_thread.start()