
import pygame as pg



class Lumbermill:
    def __init__(self, pos, resource_manager):
        image = pg.image.load("assets/graphics/building01.png")
        self.image = image
        self.name = "lumbermill"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pg.time.get_ticks()

    def update(self):
        now = pg.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["wood"] += 1
            self.resource_manager.resources["cash"] += 1
            self.resource_cooldown = now

class Stonemasonry:
    def __init__(self, pos, resource_manager):
        image = pg.image.load("assets/graphics/building02.png")
        self.image = image
        self.name = "stonemasonry"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pg.time.get_ticks()

    def update(self):
        now = pg.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["stone"] += 1
            self.resource_manager.resources["cash"] += 1
            self.resource_cooldown = now

class Farm:
    def __init__(self, pos, resource_manager):
        image = pg.image.load("assets/graphics/building03.png")
        self.image = image
        self.name = "farm"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pg.time.get_ticks()

    def update(self):
        now = pg.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["food"] += 1
            self.resource_manager.resources["cash"] += 1
            self.resource_cooldown = now

class House:
    def __init__(self, pos, resource_manager):
        image = pg.image.load("assets/graphics/house.png")
        self.image = image
        self.name = "house"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pg.time.get_ticks()
        self.rooms = 10
        self.occupants = 10

    def update(self):
        now = pg.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["food"] += 1
            self.resource_manager.resources["cash"] += 1
            self.resource_cooldown = now
        # TODO if world time < off work
        # release a worker every cooldown, let them auto assign? 

class Towncenter:
    def __init__(self, pos, resource_manager):
        image = pg.image.load("assets/graphics/towncenter.png")
        self.image = image
        self.name = "towncenter"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pg.time.get_ticks()
        self.rooms = 10
        self.occupants = 10

    def update(self):
        now = pg.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["food"] += 1
            self.resource_manager.resources["cash"] += 1
            self.resource_cooldown = now
        # TODO if world time < off work
        # release a worker every cooldown, let them auto assign? 