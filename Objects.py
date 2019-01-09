import pygame

class bee:
    speed=3

    honey=0
    honey_max=100
    left=False
    right=False
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width = 96
        self.height = 82
    def create_rect(self):
        self.rect=pygame.Rect((self.x,self.y),(self.width,self.height))

class flower:
    def __init__(self,x,y,honey):
        self.x=x
        self.y=y
        self.honey=honey
        self.width = 100
        self.height = 104
        self.rect=pygame.Rect((self.x,self.y),(self.width,self.height))

class beehive:
    honey_max=200
    def __init__(self,x,y,honey):
        self.x=x
        self.y=y
        self.honey=honey
        self.width = 150
        self.height = 117
        self.rect=pygame.Rect((self.x,self.y),(self.width,self.height))