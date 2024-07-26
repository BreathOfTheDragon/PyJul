using Sockets

HOST = "localhost"
PORT = 2042

server_socket = listen(PORT)
println("Server listening on $HOST:$PORT")

while true
    client_socket = accept(server_socket)
    println("Connected to client")
    
    while true
        try
            message = readline(client_socket)
            if isempty(message)
                println("Client disconnected.")
                break
            end
            println("Message from client is: $message")
            write(client_socket, "Got the message!\n")
        catch e
            println("Client disconnected.")
            break
        end
    end
    
    close(client_socket)
end
