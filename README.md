# City Simulator
Based on: https://github.com/scartwright91/city_builder_tutorial.git

added pathfinding library
added farm building
add food 

and cash
continuous movement for workers between tiles? 
add homes 
add daily clock to HUD
add work schedule between TC, home, and job 
update farm to be 2x2


contrl - c and arror keys should also work
how to collect all buildings job openings
how to make prople select jobs, remember housing, how would a town center work? taxes and housing? 
people should be able to make farms and housing if no house are available or no food available.  

 top down: build house/TC, build work nodes, workers auto assign during working hours
bottom up: build workers, workers randomly select a location and build a house or a farm, try to be near other houses/farms, you can also build houses and work nodes to get started.  



update HUD to include 5 buildings with room for more
workers automatically build homes near ( but not on TC) after 1 day of exploring (or start the day later)
they should search for homes and jobs available before building their own
job building have limited job opportunities

Based 



- Workers go home at night, wander during day
+ crtl c  
+ arrow keys
+ update hud with 5 buildings 
- dont walk through trees or mines 
	- dont create 5 villagers at once, one at a time
	- while at it, build through houses, not in the game window.  
	
houses should not be considered as blocked
what about TC? farms? other job sites
okay, when going into a building, you only need to be next to it 
what about getting started? 


+ todo pathfinding: if building at src, its not blocked 
+ if end is blocked, still calculate and then drop the last node? 
+ really create your own pathfinding AStar

# to test: create a house, house has 5 villagers, releases one 4 every cycle, and they immediately start exploring.  


# workers wait before overlapping on each other, or choose a new path? remember the destination?

# around night time, randomly start going home 

# search for home, if no home available, build new home (near to another home or TC or randomly)

# add mill, farm and mill worker mindset

# remember work and home

search for job or build subsistance farm 
if job and no food, quit job build subsistance farm  
