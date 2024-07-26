using Pkg
Pkg.activate("/Users/erfan/OneDrive - Colostate/Julia/Envs/env1")

using Sockets
using POMDPs
using POMDPModels
using QMDP
using POMDPTools



pomdp = TigerPOMDP()
solver = QMDPSolver()
policy = solve(solver, pomdp)

belief = [0.5, 0.5]  

function update_belief!(belief, observation)
    if observation == "tiger_left"
        belief[1] *= 0.85
        belief[2] *= 0.15
    elseif observation == "tiger_right"
        belief[1] *= 0.15
        belief[2] *= 0.85
    else
        error("Invalid observation. Please enter 'tiger_left' or 'tiger_right'.")
    end
    # Normalize 
    belief /= sum(belief)
end



HOST = "localhost"
PORT = 2042
server_socket = listen(PORT)
println("Server listening on $HOST:$PORT")



while true
    client_socket = accept(server_socket)
    println("Connected to client")
    
    while true
        # This line receives:
        obs = readline(client_socket)
        println("Observation from client is: $obs")
        
        update_belief!(belief, obs)
        policy_action = action(policy, belief)
        
        # This line transmits:
        write(client_socket, "Take action: $policy_action\n")
    end
    close(client_socket)
end


