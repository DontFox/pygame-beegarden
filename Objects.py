import pygame
from config import *
class bee:
    speed = 3
    honey = 0
    honey_max = 100
    left = False
    right = True
    first_touch = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 96
        self.height = 82

    def create_rect(self):
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def restart(self, x, y):
        self.x = x
        self.y = y
        self.honey = 0
        self.left = False
        self.right = True
        self.first_touch = False

class flower:
    def __init__(self, x, y, honey):
        self.x = x
        self.y = y
        self.honey = honey
        self.width = 100
        self.height = 104
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def restart(self,honey):
        self.honey = honey


class beehive:
    def __init__(self, x, y, honey, honey_max):
        self.x = x
        self.y = y
        self.honey = honey
        self.honey_max = honey_max
        self.width = 150
        self.height = 117
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def restart(self, honey, honey_max):
        self.honey_max = honey_max
        self.honey = honey


class enemy:
    speed = 3
    create = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 67
        self.height = 59
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def create_rect(self):
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
        self.rect2 = pygame.Rect((self.x, self.y), (self.width, height_window))
    def restart(self, x, y):
        self.x = x
        self.y = y
        self.create = False