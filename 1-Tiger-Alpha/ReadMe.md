# Tiger POMDP environment

TigerServer.jl is a Tiger POMDP environment with a random policy. Run it using julia `TigerServer.jl`  
client.py is the observer. Run it using python3 `client.py`

Note: first run the TigerServer.jl program, then run the client.py programs.

Tiger POMDP has 2 observations and 3 actions. 

Observations are: `tiger_left` and `tiger_right`. 

Actions are 0, 1 and 2. 0 denotes `listen`, 1 denotes `open left` and 2 denotes `open right`

client.py sends an observation to the TigerServer, and TigerServer responds to the client with an action according to the policy.

Note: This code is in alpha version. Policy is random. When using other policies I ran into compilation errors.
