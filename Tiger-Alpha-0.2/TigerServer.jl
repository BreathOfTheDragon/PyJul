using Pkg
Pkg.activate("/Users/erfan/OneDrive - Colostate/Julia/Envs/env1")

using Sockets
using POMDPs
using POMDPModels
using POMDPPolicies
using POMDPTools



HOST = "localhost"
PORT = 2042
server_socket = listen(PORT)
println("Server listening on $HOST:$PORT")

pomdp = TigerPOMDP()
policy = RandomPolicy(pomdp)

while true
    client_socket = accept(server_socket)
    println("Connected to client")
    
    while true
        # This line receives:
        obs = readline(client_socket)

        println("Observation from client is: $obs")
        
        policy_action = action(policy, obs)
        
        # This line transmits:
        write(client_socket, "Take action: $policy_action\n")
    end
    close(client_socket)
end
