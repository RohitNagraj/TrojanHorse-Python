import random
import socket
import threading

HOST = '127.0.0.1'
PORT = 9090


def trojan():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == 'hello':
            print("HELLO WORLD")
        client.send(f"{server_command} was executed successfully".encode('utf-8'))


def game():
    number = random.randint(0, 1000)
    tries = 1
    done = False

    while not done:
        guess = int(input("Enter a guess: "))
        if guess == number:
            done = True
            print("You WON!")
        else:
            tries += 1
            if guess > number:
                print("The actual number is smaller!")
            else:
                print("The actual number is larger!")

    print(f"You needed {tries} tries!")


