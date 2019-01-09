import pygame
from config import *
from Objects import bee, flower, beehive
from images import bg, beehive_image, bee_image_L, bee_image_R, flower_image

pygame.init()

main_window = pygame.display.set_mode((width_window, height_window))
pygame.display.set_caption('beegarden')
clock = pygame.time.Clock()

#stopwatch_config
stopwatch= pygame.time.Clock()
myfont = pygame.font.SysFont("monospace", 25)
minutes= 0
seconds= 0
milliseconds= 0
stopwatch_surf = pygame.Surface((160, 40)).convert()
stopwatch_surf.fill((220, 220, 0))


# Create Objects (see Objects.py)
#   bee (x,y)
mybee = bee(150, 200)
#   flower (x,y,honey)
flower1 = flower(580, 100, 200)
#   beehives (x,y,honey)
beehive1 = beehive(50, 300,  0)




def on_stop_at_flower():
    if mybee.honey < 100:
        if flower1.honey > 0:
            flower1.honey -= speed_honey
            mybee.honey = mybee.honey + speed_honey
def on_stop_at_beehive():
    if mybee.honey > 0:
        if beehive1.honey < beehive1.honey_max:
            mybee.honey -= speed_honey
            beehive1.honey += speed_honey


# limitsize (see config.py)
limit_down = height_window-mybee.height-limit
limit_up = limit
limit_left = limit
limit_right = width_window-mybee.width-limit


while 1:
    clock.tick(40)
# [1/3]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()




# [2/3]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if mybee.x >= limit_left:
            mybee.x -= mybee.speed
            mybee.right = False
            mybee.left = True
    if keys[pygame.K_RIGHT]:
        if mybee.x <= limit_right:
            mybee.x += mybee.speed
            mybee.right = True
            mybee.left = False
    if keys[pygame.K_UP]:
        if mybee.y >= limit_up:
            mybee.y -= mybee.speed
    if keys[pygame.K_DOWN]:
        if mybee.y <= limit_down:
            mybee.y += mybee.speed

    # check the  overlap
    mybee.create_rect()
    if mybee.rect.colliderect(flower1.rect):
        on_stop_at_flower()
    if mybee.rect.colliderect(beehive1.rect):
        on_stop_at_beehive()

    #stopwatch
    if beehive1.honey != beehive1.honey_max:
        if milliseconds > 1000:
            seconds += 1
            milliseconds -= 1000
            main_window.blit(stopwatch_surf, (0, 0))
        if seconds > 60:
            minutes += 1
            seconds -= 60
        milliseconds += stopwatch.tick_busy_loop(60)
        timelabel = myfont.render("{}:{}".format(minutes, seconds), True, (0,0,0))




    # [3/3]
    main_window.blit(bg, (0, 0))

    main_window.blit(beehive_image, (beehive1.x, beehive1.y))
    main_window.blit(flower_image, (flower1.x, flower1.y))
    if mybee.right:
        main_window.blit(bee_image_R, (mybee.x, mybee.y))
    elif mybee.left:
        main_window.blit(bee_image_L, (mybee.x, mybee.y))
    else:
        main_window.blit(bee_image_R, (mybee.x, mybee.y))

    main_window.blit(timelabel,(0, 0))

    pygame.display.update()

    print(mybee.honey, '  ', flower1.honey, '  ', beehive1.honey)




pygame.quit()
