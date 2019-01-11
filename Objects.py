import pygame


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
        self.left=False
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
        self.honey=honey


class beehive:
    honey_max = 200

    def __init__(self, x, y, honey):
        self.x = x
        self.y = y
        self.honey = honey
        self.width = 150
        self.height = 117
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def restart(self,honey):
        self.honey=honey


class enemy:
    speed = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 150
        self.height = 117
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def create_rect(self):
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
    def restart(self):
        None