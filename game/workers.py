
import pygame as pg
import random
# from pathfinding.core.diagonal_movement import DiagonalMovement
#rom pathfinding.core.grid import Grid
#rom pathfinding.finder.a_star import AStarFinder
from .pathfinder import AStarFinder



class Worker:

    def __init__(self, name, tile, world):
        self.name = name
        print(self.name)
        self.world = world
        self.world.entities.append(self)
        image = pg.image.load("assets/graphics/worker.png").convert_alpha()
        self.name = "worker"
        self.image = pg.transform.scale(image, (image.get_width()*2, image.get_height()*2))
        self.tile = tile

        # pathfinding
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = self
        self.move_timer = pg.time.get_ticks()
        
        self.path = []
        self.create_path()
        
        self.offwork = random.gauss(1 * 60, 3) # ~1 minute
        self.home = [0,0] # address
        self.work = [0,0] # address
        
    def create_path(self, endx = None, endy = None):
        for row in self.world.collision_matrix:
            pass # print(row)
        searching_for_path = True
        while searching_for_path:
            x = endx if endx is not None and isinstance(endx, int) else random.randint(0, self.world.grid_length_x - 1)
            y = endy if endy is not None and isinstance(endy, int) else random.randint(0, self.world.grid_length_y - 1)
            dest_tile = self.world.world[x][y]
            if not dest_tile["collision"]:
                self.start = [self.tile["grid"][0], self.tile["grid"][1]]
                self.end = [x, y]
                finder = AStarFinder() 
                self.path_index = 0
                    
                self.path = finder.find_path(self.start, self.end, self.world.collision_matrix)
                searching_for_path = False
                
    def change_tile(self, new_tile):
        self.world.workers[self.tile["grid"][0]][self.tile["grid"][1]] = None
        # print(new_tile)
        self.world.workers[new_tile[0]][new_tile[1]] = self
        self.tile = self.world.world[new_tile[0]][new_tile[1]]
        
    def step (self):
        try: # try to move if there are steps, otherwise just stay still 
            # update position in the world
            self.change_tile( self.path[self.path_index] )
            self.path_index += 1 # update path index
        except: 
            return

    def update(self):
        now = pg.time.get_ticks()
        if now - self.move_timer < 1000:
            return; # skip time between each move
        self.step()
        self.move_timer = now # update clock
        if self.world.resource_manager.time >= self.offwork and new_pos != (25, 25): # if outside of 25, 25 after off work
            self.create_path(25, 25)
        elif self.path_index >= len(self.path) - 1 and self.world.resource_manager.time < self.offwork:
            self.create_path()


