# Code Details

Splendid News! Eversince using MacOS I can FINALLY compile the packages!

TigerServer2.jl is a Tiger POMDP environment with a QMDP policy. Run it using `julia TigerServer2.jl`  
Client.py is the observer. Run it using `python3 Client.py`  

Note: first run the TigerServer2.jl program, then run the Client.py program.

Tiger POMDP has 2 observations and 3 actions. 

Observations are: `tiger_left` and `tiger_right`. 

Actions are 0, 1 and 2. 0 denotes `listen`, 1 denotes `open the left door` and 2 denotes `open the right door`

Client.py sends an observation to the TigerServer2, and TigerServer2 responds to the Client with an action according to the policy(In this case, the policy solver is QMDP).

Note: This code is in alpha version 0.2. Policy uses a QMDP solver. 


# Tiger POMDP Environment Explanation


The Tiger POMDP environment is a Partially Observable Markov Decision Process environment.   

In this scenario, an agent must choose between two doors: one hides a tiger (resulting in a penalty if opened), and the other hides treasure (resulting in a reward if opened).   

The agent has three possible actions: `open the left door`, `open the right door`, or `listen` for the tiger's location.  

The listening action provides a noisy observation with two possible outcomes: hearing the tiger on the left or hearing the tiger on the right. 

The goal is to maximize the total reward by strategically balancing the costs and benefits of listening and choosing which door to open based on uncertain observations.

