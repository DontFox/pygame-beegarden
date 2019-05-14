import pygame
from config import *


class bee:
    speed = 4.5
    honey = 0
    honey2 = 0
    honey_max = 100
    left = False
    right = True
    first_touch = False
    bubble = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 53
        self.height = 45

    def create_rect(self):
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def restart(self, x, y):
        self.x = x
        self.y = y
        self.honey = 0
        self.honey2 = 0
        self.left = False
        self.right = True
        self.first_touch = False


class flower:
    def __init__(self, x, y, honey):
        self.x = x
        self.y = y
        self.honey = honey
        self.width = flower_width
        self.height = flower_height
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def restart(self,honey):
        self.honey = honey


class beehive:
    honey = 0

    def __init__(self, x, y, honey_max):
        self.x = x
        self.y = y
        self.honey_max = honey_max

        self.width = 83
        self.height = 64
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def restart(self, honey, honey_max):
        self.honey_max = honey_max
        self.honey = honey


class enemy:
    speed = 6

    def __init__(self, x, y, create):
        self.x = x
        self.y = y
        self.width = 24
        self.height = 32
        self.create = create
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def create_rect(self):
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
        self.rect2 = pygame.Rect((self.x, self.y), (self.width, height_window))

    def restart(self, x, y):
        self.x = x
        self.y = y
        self.create = False


class obstacle(enemy):

    def __init__(self, x, y, width, height, create):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.create = create
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
