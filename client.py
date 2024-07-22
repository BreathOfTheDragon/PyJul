import socket

HOST = "localhost"
PORT = 2042

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT))

while True:
    message = input("Enter message to send to server: ")
    socket.send((message + "\n").encode('utf-8'))
    print(socket.recv(1024).decode('utf-8'))
