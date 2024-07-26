using Pkg
Pkg.activate("/Users/erfan/OneDrive - Colostate/Julia/Envs/env1")

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

while true
    println("Please enter observation: tiger_left or tiger_right")
    obs = readline()
    update_belief!(belief, obs)
    policy_action = action(policy, belief)
    println("Action for observation $obs: $policy_action")
end