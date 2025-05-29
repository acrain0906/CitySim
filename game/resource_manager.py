
import pygame as pg
import time



class ResourceManager:


    def __init__(self):
        
        self.length_of_day =  60 
        self.length_of_day *= 16 # 16 minutes
        self.time_start = time.time() % self.length_of_day 
        self.time = (time.time() % self.max_length_day ) - self.time_start

        # resources
        self.resources = {
            "wood": 10,
            "stone": 10,
            "food" : 10, 
            "cash" : 100
        }

        # costs
        self.costs = {
            "lumbermill": {"food": 7, "stone": 4, "cash" : 10},
            "stonemasonry": {"food": 7, "wood": 5, "cash" : 10},
            "farm": {"wood": 1, "stone": 0, "cash" : 2},
            "house": {"food": 7, "wood": 5, "cash" : 10},
            "towncenter": {"food": 7, "wood": 5, "cash" : 10}
        }

    def apply_cost_to_resource(self, building):
        for resource, cost in self.costs[building].items():
            self.resources[resource] -= cost

    def is_affordable(self, building):
        affordable = True
        for resource, cost in self.costs[building].items():
            if cost > self.resources[resource]:
                affordable = False
        return affordable
        
    def tick(self):
        self.time = (time.time() % self.max_length_day ) - self.time_start