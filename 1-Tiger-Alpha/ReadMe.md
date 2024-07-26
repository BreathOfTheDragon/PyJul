TigerServer.jl is a Tiger POMDP env with a random policy. Run it using julia `TigerServer.jl`  
client.py is the observer. Run it using python3 `client.py`

Tiger POMDP has 2 observations and 3 actions. Observations are: `tiger_left` and `tiger_right`. Actions are 0, 1 and 2. 0 denotes `listen`, 1 denotes `open left` and 2 denotes `open right`
