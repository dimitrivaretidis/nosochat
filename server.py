import socket
import threading
from datetime import datetime

HOST = '0.0.0.0'
PORT = 5555

clients = []
names = []

def tijd():
    return datetime.now().strftime("[%H:%M:%S]")


def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                broadcast(message)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                name = names[index]
                broadcast(f"{tijd()} {name} heeft de chat verlaten.".encode('utf-8'))
                names.remove(name)
                client.close()
                break


def receive():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Server draait...")

    while True:
        client, address = server.accept()
        print(f"Verbonden met {str(address)}")

        client.send('NAAM'.encode('utf-8'))
        name = client.recv(1024).decode('utf-8')

        names.append(name)
        clients.append(client)

        print(f"Naam van gebruiker: {name}")
        broadcast(f"{tijd()} {name} is de chat binnengekomen!".encode('utf-8'))
        client.send('Verbonden met de server!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()