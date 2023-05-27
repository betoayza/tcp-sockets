#!/usr/bin/python3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
host = "192.168.0.5"
port = 444

print(host)

server_socket.bind((host, port))
server_socket.listen(4)  # especify max connections number

while True:
    client_socket, address = server_socket.accept()

    print(f"Client: {address} is talking to this server...")

    message = "Hey, client, thanks to communicate with me!"
    client_socket.send(message.encode('ascii'))
    client_socket.close()
