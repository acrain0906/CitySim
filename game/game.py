import pygame as pg
import sys
from .world import World
from .settings import TILE_SIZE
from .utils import draw_text
from .camera import Camera
from .hud import Hud
from .resource_manager import ResourceManager
from .workers import Worker
import random


names = [
'Austin',
'John',
'Patrick',
'Rubin',
'Jason',
'Joyce',
'Rachel',
'Howard',
'Sue',
'Laura',
'Jacqueline',
'Jack',
'Sherry',
'Miranda',
'Camy',
'Laurie',
'Byron',
'Ceci',
'Erin',
'Jess',
'Gary',
'Karis',
'Alyssa',
'Madison',
'Michelle',
'Shari',
'Andy',
'Keegan',
'Kitara',
'Greg',
'Cindy',
'Dane',
'Logan',
'Carla',
'Michael',
'Kathy',
'Jim',
'Carlos',
'Joe',
'Amanda',
'Astha',
'Shagun',
'Kiki',
'Kenneth',
'Yukti',
'Krissy'
]

def printMat(mat):
    for i in range(len(mat)):
        s = ''
        for j in range(len(mat[0])):
            s += f'{mat[i][j]} '
        print (s) 

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        # entities
        self.entities = []

        # resource manager
        self.resource_manager = ResourceManager()

        # hud
        self.hud = Hud(self.resource_manager, self.width, self.height)

        # world
        self.world = World(self.resource_manager, self.entities, self.hud, 50, 50, self.width, self.height)
        for _ in range(10): Worker(names[random.randint(0, len(names)-1)], self.world.world[25][25], self.world)
        # printMat(self.world.collision_matrix)

        # camera
        self.camera = Camera(self.width, self.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c and pg.key.get_mods() & pg.KMOD_CTRL:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_ESCAPE:
                    self.playing = False

    def update(self):
        self.camera.update()
        for e in self.entities: e.update()
        self.hud.update()
        self.world.update(self.camera)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.world.draw(self.screen, self.camera)
        self.hud.draw(self.screen)

        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (50, 10)
        )

        pg.display.flip()

