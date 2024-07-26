# Tiger POMDP environment

Splendid News! Eversince using MacOS I can FINALLY compile the packages!

TigerServer2.jl is a Tiger POMDP environment with a QMDP policy. Run it using `julia TigerServer2.jl`  
Client.py is the observer. Run it using `python3 Client.py`  

Note: first run the TigerServer2.jl program, then run the Client.py program.

Tiger POMDP has 2 observations and 3 actions. 

Observations are: `tiger_left` and `tiger_right`. 

Actions are 0, 1 and 2. 0 denotes `listen`, 1 denotes `open left` and 2 denotes `open right`

Client.py sends an observation to the TigerServer2, and TigerServer2 responds to the Client with an action according to the policy(In this case, the policy solver is QMDP).

Note: This code is in alpha version 0.2. Policy uses a QMDP solver. 
