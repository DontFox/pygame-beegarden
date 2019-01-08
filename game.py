import pygame
import sys, random

pygame.init()

#window size
width_window = 807
height_window = 454

main_window = pygame.display.set_mode((width_window,height_window))
pygame.display.set_caption('beegarden')
clock=pygame.time.Clock()



# load images
#   Background
bg = pygame.image.load('background.jpg')
#   bee,beehive,flower
bee_image=pygame.image.load('bee.png')
beehive_image=pygame.image.load('beehive.png')
flower_image=pygame.image.load('flower.png')

speed_honey=1


# config bee
class bee:
    speed=3
    width=96
    height=82
    honey=0
    honey_max=100
    def __init__(self,x,y):
        self.x=x
        self.y=y

class flower:
    def __init__(self,x,y,honey):
        self.x=x
        self.y=y
        self.honey=honey

class beehive:
    honey_max=200
    def __init__(self,x,y,honey):
        self.x=x
        self.y=y
        self.honey=honey



# Create Objects
#   bee (x,y)
mybee=bee(150,200)
#   flower (honey)
flower1=flower(580,100,200)
#   beehives (honey)
beehive1=beehive(50,300,0)


rect1=pygame.Rect((flower1.x,flower1.y,104,100)) #rect for flower
rect2=pygame.Rect((beehive1.x,beehive1.y,150,117))

def on_stop_at_flower():
    if mybee.honey<100:
        if flower1.honey>0:
            flower1.honey-=speed_honey
            mybee.honey = mybee.honey + speed_honey
def on_stop_at_beehive():
    if mybee.honey > 0:
        if beehive1.honey<beehive1.honey_max:
            mybee.honey-=speed_honey
            beehive1.honey+=speed_honey


# limitsize
limit=8
limit_down=height_window-mybee.height-limit
limit_up=limit
limit_left=limit
limit_right=width_window-mybee.width-limit


i=1
while 1:
    clock.tick(40)
# [1/3]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()




# [2/3]
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if mybee.x>=limit_left:
            mybee.x -= mybee.speed
    if keys[pygame.K_RIGHT]:
        if mybee.x<=limit_right:
            mybee.x += mybee.speed
    if keys[pygame.K_UP]:
        if mybee.y>=limit_up:
            mybee.y -= mybee.speed
    if keys[pygame.K_DOWN]:
        if mybee.y<=limit_down:
            mybee.y += mybee.speed

    if mybee.x+mybee.width>rect1.x and mybee.y<rect1.y+rect1.height:
        on_stop_at_flower()



# [3/3]
    main_window.blit(bg, (0, 0))

    main_window.blit(beehive_image,(beehive1.x,beehive1.y))
    main_window.blit(flower_image, (flower1.x,flower1.y))
    main_window.blit(bee_image, (mybee.x,mybee.y))
    pygame.display.update()

    print(mybee.honey,'  ',flower1.honey,'  ',beehive1.honey)




pygame.quit()