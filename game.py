import pygame, random
from pygame.locals import *

import pygameMenu
from pygameMenu.locals import *

from config import *
from Objects import bee, flower, beehive, enemy
from images import bg, beehive_image, bee_image_L, bee_image_R, flower_image,enemy_image

# -----------------------------------------------------------------------------

# Init pygame

pygame.init()

main_window = pygame.display.set_mode((width_window,
                                       height_window))
pygame.display.set_caption('bee-haney')
clock = pygame.time.Clock()

# -----------------------------------------------------------------------------

# stopwatch_config

stopwatch= pygame.time.Clock()
myfont = pygame.font.SysFont("monospace", 25,bold=True)
stopwatch_surf = pygame.Surface((160, 40)).convert()

# -----------------------------------------------------------------------------

# Create Objects (see Objects.py)

#   bee (x,y)
mybee = bee(bee_start_point_x, bee_start_point_y)

#   flower (x,y,honey)
flower1 = flower(width_window-300,
                 150,
                 honey_flower
                 )

#   beehives (x,y,honey)
beehive1 = beehive(75,
                   height_window-50-117,
                   0,
                   flower1.honey
                   )

#   falling enemy
enemy1 = enemy(random.randint(0 + limit, width_window - limit), 0)
enemy2 = enemy(random.randint(0 + limit, width_window - limit), 0)
enemy3 = enemy(random.randint(0 + limit, width_window - limit), 0)
enemy4 = enemy(random.randint(0 + limit, width_window - limit), 0)

# -----------------------------------------------------------------------------

# honeycount (see config.py)

honeycount_surf=pygame.Surface((honeycount_width,honeycount_height)).convert()

# -----------------------------------------------------------------------------

# limitsize (see config.py)

limit_down = height_window-mybee.height-limit
limit_up = limit
limit_left = limit
limit_right = width_window-mybee.width-limit

# -----------------------------------------------------------------------------


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


def restart():
    global stopwatch, minutes, seconds, milliseconds
    stopwatch = pygame.time.Clock()
    minutes = 0
    seconds = 0
    milliseconds = 0
    mybee.restart(bee_start_point_x,bee_start_point_y)
    flower1.restart(honey_flower)
    beehive1.restart(0,flower1.honey)
    enemy1.restart(random.randint(0 + limit, width_window - limit), 0)
    enemy2.restart(random.randint(0 + limit, width_window - limit), 0)
    enemy3.restart(random.randint(0 + limit, width_window - limit), 0)
    enemy4.restart(random.randint(0 + limit, width_window - limit), 0)


def falling_enemy():

    global enemy1, enemy2, enemy3, enemy4

    if beehive1.honey != beehive1.honey_max:
        #enemy1
        if mybee.first_touch:
            enemy1.create = True
            if enemy1.y>height_window:
                enemy1 = enemy(random.randint(0 + limit, width_window - limit-enemy1.width), 0)
            enemy1.y += enemy1.speed
            if mybee.rect.colliderect(enemy1.rect):
                restart()
            enemy1.create_rect()
        #enemy 2
        if seconds >= 10 or minutes>=1:
            enemy2.create = True
            # if enemy1.create:
            #     if enemy2.rect2.colliderect(enemy1.rect2):
            #         enemy2 = enemy(random.randint(0 + limit, width_window - limit - enemy2.width), 0)
            # if enemy3.create:
            #     if enemy2.rect2.colliderect(enemy3.rect2):
            #         enemy2 = enemy(random.randint(0 + limit, width_window - limit - enemy2.width), 0)
            # if enemy4.create:
            #     if enemy2.rect2.colliderect(enemy4.rect2):
            #         enemy2 = enemy(random.randint(0 + limit, width_window - limit - enemy2.width), 0)
            # # if enemy2.rect2.colliderect(enemy1.rect2) or enemy2.rect2.colliderect(enemy3.rect2) or enemy2.rect2.colliderect(enemy4.rect2):
            # #     enemy2 = enemy(random.randint(0 + limit, width_window - limit - enemy2.width), 0)
            if enemy2.y>height_window:
                enemy2 = enemy(random.randint(0 + limit, width_window - limit-enemy2.width), 0)
            enemy2.y += enemy2.speed
            if mybee.rect.colliderect(enemy2.rect):
                restart()
            enemy2.create_rect()
        #enemy3
        if seconds >= 20 or minutes>=1:
            enemy3.create = True
            # if enemy1.create:
            #     if enemy3.rect2.colliderect(enemy1.rect2):
            #         enemy3 = enemy(random.randint(0 + limit, width_window - limit - enemy3.width), 0)
            # if enemy2.create:
            #     if enemy3.rect2.colliderect(enemy2.rect2):
            #         enemy3 = enemy(random.randint(0 + limit, width_window - limit - enemy3.width), 0)
            # if enemy4.create:
            #     if enemy3.rect2.colliderect(enemy4.rect2):
            #         enemy3 = enemy(random.randint(0 + limit, width_window - limit - enemy3.width), 0)
            # # if enemy3.rect2.colliderect(enemy1.rect2) or enemy3.rect2.colliderect(enemy2.rect2) or enemy3.rect2.colliderect(enemy4.rect2):
            # #     enemy3 = enemy(random.randint(0 + limit, width_window - limit - enemy3.width), 0)
            if enemy3.y>height_window:
                enemy3 = enemy(random.randint(0 + limit, width_window - limit-enemy3.width), 0)
            enemy3.y += enemy3.speed
            if mybee.rect.colliderect(enemy3.rect):
                restart()
            enemy3.create_rect()
        #enemy4
        if minutes >= 1:
            enemy4.create = True
            # if enemy4.rect2.colliderect(enemy1.rect2) or enemy4.rect2.colliderect(enemy2.rect2) or enemy4.rect2.colliderect(enemy3.rect2):
            #     enemy4 = enemy(random.randint(0 + limit, width_window - limit - enemy4.width), 0)
            if enemy4.y>height_window:
                enemy4 = enemy(random.randint(0 + limit, width_window - limit-enemy4.width), 0)
            enemy4.y += enemy4.speed
            if mybee.rect.colliderect(enemy4.rect):
                restart()
            enemy4.create_rect()
    else:
        enemy1.create = False
        enemy2.create = False
        enemy3.create = False
        enemy4.create = False


def maingame():

    global  honeycount_label
    global timelabel
    global minutes, seconds
    global milliseconds, stopwatch

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if mybee.x >= limit_left:
            mybee.x -= mybee.speed
            mybee.right = False
            mybee.left = True
            mybee.first_touch = True
    if keys[pygame.K_RIGHT]:
        if mybee.x <= limit_right:
            mybee.x += mybee.speed
            mybee.right = True
            mybee.left = False
            mybee.first_touch = True
    if keys[pygame.K_UP]:
        if mybee.y >= limit_up:
            mybee.y -= mybee.speed
            mybee.first_touch = True
    if keys[pygame.K_DOWN]:
        if mybee.y <= limit_down:
            mybee.y += mybee.speed
            mybee.first_touch = True

    # check the  overlap
    mybee.create_rect()
    if mybee.rect.colliderect(flower1.rect):
        on_stop_at_flower()
    if mybee.rect.colliderect(beehive1.rect):
        on_stop_at_beehive()

    # honeycount
    honeycount_label = myfont.render('Bee:{} Beehive:{} Flower:{}'.format(mybee.honey,
                                                                          beehive1.honey,
                                                                          flower1.honey), True, (0, 0, 0))

    # stopwatch
    if mybee.first_touch:
        if minutes == 0 and seconds == 0:
            stopwatch = pygame.time.Clock()
        if beehive1.honey != beehive1.honey_max:
            if milliseconds > 1000:
                seconds += 1
                milliseconds -= 1000
                main_window.blit(stopwatch_surf, (0, 0))
            if seconds > 60:
                minutes += 1
                seconds -= 60
            milliseconds += stopwatch.tick_busy_loop(60)

    timelabel = myfont.render("{}:{}".format(minutes, seconds),
                              True,
                              (0, 0, 0)
                              )

    # enemies
    falling_enemy()

def draw_window():
    main_window.blit(bg, (0, 0))

    main_window.blit(beehive_image, (beehive1.x, beehive1.y))
    main_window.blit(flower_image, (flower1.x, flower1.y))

    if mybee.right:
        main_window.blit(bee_image_R,(mybee.x, mybee.y))
    elif mybee.left:
        main_window.blit(bee_image_L, (mybee.x, mybee.y))
    if enemy1.create:
        main_window.blit(enemy_image, (enemy1.x, enemy1.y))
    if enemy2.create:
        main_window.blit(enemy_image, (enemy2.x, enemy2.y))
    if enemy3.create:
        main_window.blit(enemy_image, (enemy3.x, enemy3.y))
    if enemy4.create:
        main_window.blit(enemy_image, (enemy4.x, enemy4.y))

    main_window.blit(timelabel, (0, 0))
    main_window.blit(honeycount_label, (width_window - honeycount_width, height_window - honeycount_height))

# defs for Menu

def mainmenu_background():

    main_window.fill((40, 0, 40))

# -----------------------------------------------------------------------------

# MainMenu

main_menu = pygameMenu.Menu(main_window,
                            window_width=width_window,
                            window_height=height_window,
                            font=pygameMenu.fonts.FONT_NEVIS,
                            title='Main Menu',
                            bgfun=mainmenu_background,
                            menu_color_title=(0, 0, 0),
                            enabled = True,
                            menu_alpha = 90
                            )



# -----------------------------------------------------------------------------


while 1:

    # [1/3]

    clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                main_menu.enable()




    # [2/3]

    maingame()



    # [3/3]

    draw_window()

    pygame.display.flip()



pygame.quit()
