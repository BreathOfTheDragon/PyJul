using Sockets

HOST = "localhost"
PORT = 2042

client_socket = connect(HOST, PORT)

while true
    print("Enter message to send to server: ")
    message = readline(stdin)
    write(client_socket, message * "\n")
    response = readline(client_socket)
    println(response)
end

close(client_socket)
