import socket


HOST = "localhost"
PORT = 2042
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(42)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    while True:
        message = communication_socket.recv(1024).decode('utf-8')
        print(f"Message from client is: {message}")
        communication_socket.send(f"Got the message!".encode('utf-8'))

    communication_socket.close()