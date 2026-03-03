import socket
import threading
from datetime import datetime

HOST = input("Voer het IP-adres van de server in: ")
PORT = int(input("Voer de poort in: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Voer je naam in: ")


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NAAM':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print("Er is een fout opgetreden!")
            client.close()
            break


def write():
    while True:
        message = input("")
        tijd = datetime.now().strftime("[%H:%M:%S]")
        client.send(f"{tijd} {name}: {message}".encode('utf-8'))


def credits():
    print("-Credits-")
    print("Gemaakt door D.V. Nosoman")


def menu():
    while True:
        print("-Menu-")
        print("1. Chat")
        print("2. Credits")
        keuze = input("Maak een keuze: ")

        if keuze == '1':
            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()
            break

        elif keuze == '2':
            credits()
        else:
            print("Ongeldige keuze!")

menu()