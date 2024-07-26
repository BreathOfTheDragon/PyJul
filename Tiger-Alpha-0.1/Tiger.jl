using Pkg
Pkg.activate("/Users/erfan/OneDrive - Colostate/Julia/Envs/env1")

using POMDPs
using POMDPModels
using POMDPPolicies
using POMDPTools


pomdp = TigerPOMDP()
policy = RandomPolicy(pomdp)
println("Please enter observation: tiger_left or tiger_right")
obs = readline()
policy_action = action(policy, obs)
println("Action for observation $obs: $policy_action")
