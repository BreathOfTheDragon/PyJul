using Sockets

HOST = "localhost"
PORT = 2042
server_socket = listen(PORT)
println("Server listening on $HOST:$PORT")



while true
    client_socket = accept(server_socket)
    println("Connected to client")
    
    while true
        # This line receives:
        message = readline(client_socket)

        println("Message from client is: $message")

        # This line transmits:
        write(client_socket, "$message\n")
    end
    close(client_socket)
end
