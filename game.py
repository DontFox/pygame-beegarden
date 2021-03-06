import pygame, random
from pygame.locals import *

import pygameMenu
from pygameMenu.locals import *

from config import *
from Objects import bee, flower, beehive, enemy
from images import bg, beehive_image, bee_image_L, bee_image_R, flower_image, enemy_image

# -----------------------------------------------------------------------------

# Init pygame

pygame.init()

main_window = pygame.display.set_mode((width_window, height_window))
pygame.display.set_caption('Bee in the forest. How to collect all the pollen?')
pygame.display.set_icon(pygame.image.load("icon.ico"))

clock = pygame.time.Clock()

DIFFICULTY = ['EASY']

__author__='Dmitry "DF" Kraychik'
HELP = ['Move - - - - UP, DOWN, LEFT, RIGHT', 'Give/Take Honey - - - - "F","G"']
ABOUT = ['pygame {}'.format(pygame.__version__), 'PyGameMenu {}'.format(pygameMenu.__version__)]

# -----------------------------------------------------------------------------

# stopwatch_config

stopwatch = pygame.time.Clock()
myfont = pygame.font.SysFont("monospace", 25, bold=True)
stopwatch_surf = pygame.Surface((160, 40)).convert()

# -----------------------------------------------------------------------------

# Create Objects (see Objects.py)

#   bee (x,y)
mybee = bee(bee_start_point_x, bee_start_point_y)
#   flower (x,y,honey)
flower1 = flower(600,
                 379,
                 honey_flower
                 )
#  flower 2 (hard mode)
flower2 = flower(800,
                 379,honey_flower)

#   beehives (x,y,honey)
beehive1 = beehive(115,
                   379,
                   flower1.honey,
                   )
beehive2 = beehive(210,
                   379,
                   flower2.honey
                   )

#   falling enemy
enemy1 = enemy(random.randint(0 + limit, width_window - limit), 0, False)
enemy2 = enemy(random.randint(0 + limit, width_window - limit), 0, False)
enemy3 = enemy(random.randint(0 + limit, width_window - limit), 0, False)
enemy4 = enemy(random.randint(0 + limit, width_window - limit), 0, False)
enemy5 = enemy(random.randint(0 + limit, width_window - limit), 0, False)


# -----------------------------------------------------------------------------

# honeycount (see config.py)

honeycount_surf = pygame.Surface((honeycount_width, honeycount_height)).convert()
honeycount_surf2 = pygame.Surface((honeycount_width, honeycount_height)).convert()

# -----------------------------------------------------------------------------

# limitsize (see config.py)

limit_down = height_window-mybee.height-limit-35
limit_up = limit
limit_left = limit
limit_right = width_window-mybee.width-limit

# -----------------------------------------------------------------------------

# Pumping honey
def on_stop_at_flower():
    if mybee.honey2 <= 0:
        if mybee.honey < 100:
            if flower1.honey > 0:
                flower1.honey -= speed_honey
                mybee.honey = mybee.honey + speed_honey

def on_stop_at_flower2():
    if mybee.honey <= 0:
        if mybee.honey2 < 100:
            if flower2.honey > 0:
                flower2.honey -= speed_honey
                mybee.honey2 += speed_honey

def on_stop_at_beehive():
    if mybee.honey > 0:
        if beehive1.honey < beehive1.honey_max:
            mybee.honey -= speed_honey
            beehive1.honey += speed_honey
def on_stop_at_beehive2():
    if mybee.honey2 > 0:
        if beehive2.honey < beehive2.honey_max:
            mybee.honey2 -=speed_honey
            beehive2.honey += speed_honey



def restart():
    global stopwatch, minutes, seconds, milliseconds
    stopwatch = pygame.time.Clock()
    minutes = 0
    seconds = 0
    milliseconds = 0
    mybee.restart(bee_start_point_x,bee_start_point_y)
    flower1.restart(honey_flower)
    flower2.restart(honey_flower)
    beehive1.restart(0,flower1.honey)
    beehive2.restart(0,flower2.honey)
    enemy1.restart(random.randint(0 + limit, width_window - limit), 0)
    enemy2.restart(random.randint(0 + limit, width_window - limit), 0)
    enemy3.restart(random.randint(0 + limit, width_window - limit), 0)
    enemy4.restart(random.randint(0 + limit, width_window - limit), 0)
    enemy5.restart(random.randint(0 + limit, width_window - limit), 0)


def falling_enemy():

    global enemy1, enemy2, enemy3, enemy4, enemy5

    if beehive1.honey != beehive1.honey_max or beehive2.honey != beehive2.honey_max:

        #enemy1

        if enemy1.create and mybee.first_touch:
            if enemy1.y > height_window:
                enemy1 = enemy(random.randint(0 + limit, width_window - limit-enemy1.width), 0, True)
            enemy1.y += enemy1.speed
            if mybee.rect.colliderect(enemy1.rect):
                restart()

            enemy1.create_rect()

        #enemy 2

        if enemy2.create and mybee.first_touch:
            if seconds >= 1 or minutes >= 1:
                if enemy2.y>height_window:
                    enemy2 = enemy(random.randint(0 + limit, width_window - limit-enemy2.width), 0, True)
                enemy2.y += enemy2.speed
                if mybee.rect.colliderect(enemy2.rect):
                    restart()
                enemy2.create_rect()

        #enemy3

        if enemy3.create and mybee.first_touch:
            if seconds >=2 or minutes >= 1:
                if enemy3.y>height_window:
                    enemy3 = enemy(random.randint(0 + limit, width_window - limit-enemy3.width), 0, True)
                enemy3.y += enemy3.speed
                if mybee.rect.colliderect(enemy3.rect):
                    restart()
                enemy3.create_rect()

        #enemy4

        if enemy4.create and mybee.first_touch:
            if seconds >=3 or minutes >=1:
                if enemy4.y>height_window:
                    enemy4 = enemy(random.randint(0 + limit, width_window - limit-enemy4.width), 0, True)
                enemy4.y += enemy4.speed
                if mybee.rect.colliderect(enemy4.rect):
                    restart()
                enemy4.create_rect()


        if enemy5.create and mybee.first_touch:
            if seconds >= 4 or minutes >= 1:
                if enemy5.y>height_window:
                    enemy5 = enemy(random.randint(0 + limit, width_window - limit-enemy5.width), 0, True)
                enemy5.y += enemy5.speed
                if mybee.rect.colliderect(enemy5.rect):
                    restart()
                enemy5.create_rect()
    else:
        enemy1.create = False
        enemy2.create = False
        enemy3.create = False
        enemy4.create = False
        enemy5.create = False



def maingame(difficulty):
    global honeycount_label, timelabel, minutes, seconds, milliseconds, stopwatch, clock
    global enemy1,enemy2,enemy3,enemy4, enemy5, beehive1

    restart()

    difficulty = difficulty[0]

    if difficulty == 'EASY':
        enemy1.create = True
        enemy2.create = True
        honey_flower = 200
    elif difficulty == 'MEDIUM':
        enemy1.create = True
        enemy2.create = True
        enemy3.create = True
        honey_flower = 300
    elif difficulty == 'HARD':
        enemy1.create = True
        enemy2.create = True
        enemy3.create = True
        enemy4.create = True
        honey_flower = 500
    elif difficulty == "VERY HARD":
        enemy1.create = True
        enemy2.create = True
        enemy3.create = True
        enemy4.create = True
        enemy5.create = True

        honey_flower = 700

    flower1.restart(honey_flower)
    flower2.restart(honey_flower)
    beehive1.restart(0, flower1.honey)
    beehive2.restart(0, flower2.honey)

    main_menu.disable()
    main_menu.reset(1)

    while 1:
        clock.tick(60)
        playevents = pygame.event.get()
        for e in playevents:
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE and main_menu.is_disabled():
                    main_menu.enable()
                    return
        if beehive1.honey == beehive1.honey_max and beehive2.honey == beehive2.honey_max:
            main_menu.enable()
            return

        mybee.create_rect()

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

        # перекачка мёда
        if keys[pygame.K_f] and mybee.rect.colliderect(flower1.rect):
            on_stop_at_flower()
        if keys[pygame.K_g] and mybee.rect.colliderect(flower2.rect):
            on_stop_at_flower2()
        if keys[pygame.K_f] and mybee.rect.colliderect(beehive1.rect)and not(keys[pygame.K_g]):
            on_stop_at_beehive()
        if keys[pygame.K_g] and mybee.rect.colliderect(beehive2.rect)and not(keys[pygame.K_f]):
            on_stop_at_beehive2()

        # check the  overlap
        mybee.create_rect()

        # labels for count
        beehive1_label = myfont.render('{}'.format(beehive1.honey), True, (255, 50, 120))
        beehive2_label = myfont.render('{}'.format(beehive2.honey), True, (50, 120, 255))
        flower1_label = myfont.render('{}'.format(flower1.honey), True, (255, 50, 120))
        flower2_label = myfont.render('{}'.format(flower2.honey), True, (50, 120, 255))

        # stopwatch
        if mybee.first_touch:
            if minutes == 0 and seconds == 0:
                stopwatch = pygame.time.Clock()
            if 1:
                if milliseconds > 1000:
                    seconds += 1
                    milliseconds -= 1000
                    main_window.blit(stopwatch_surf, (0, 0))
                if seconds > 59:
                    minutes += 1
                    seconds -= 60
                milliseconds += stopwatch.tick_busy_loop(60)

        # label for stopwatch
        timelabel = myfont.render("{}:{}".format(minutes, seconds), True, (255, 255, 255), (15, 15, 15))

        # enemies
        falling_enemy()

        if (enemy1.create or enemy2.create or enemy3.create or enemy4.create or enemy5.create) == False:
            main_menu.enable()
            return


        main_window.blit(bg, (0, 0))

        main_window.blit(beehive_image, (beehive1.x, beehive1.y))
        main_window.blit(beehive_image, (beehive2.x, beehive2.y))
        main_window.blit(flower_image, (flower1.x, flower1.y))
        main_window.blit(flower_image, (flower2.x,flower2.y))

        if mybee.right:
            main_window.blit(bee_image_R,(mybee.x, mybee.y))
        elif mybee.left:
            main_window.blit(bee_image_L, (mybee.x, mybee.y))
        if enemy1.create:
            main_window.blit(enemy_image, (enemy1.x, enemy1.y))
        if enemy2.create:
            if seconds >= 1 or minutes >= 1:
                main_window.blit(enemy_image, (enemy2.x, enemy2.y))
        if enemy3.create:
            if seconds >= 2 or minutes >= 1:
                main_window.blit(enemy_image, (enemy3.x, enemy3.y))
        if enemy4.create:
            if seconds >= 3 or minutes >= 1:
                main_window.blit(enemy_image, (enemy4.x, enemy4.y))
        if enemy5.create:
            if seconds >= 6 or minutes >= 1:
                main_window.blit(enemy_image, (enemy5.x, enemy5.y))

        main_window.blit(timelabel, (488, 0))
        main_window.blit(beehive1_label, (135, 448))
        main_window.blit(beehive2_label, (230, 448))
        main_window.blit(flower1_label, (608, 448))
        main_window.blit(flower2_label, (808, 448))

        pygame.display.flip()


# defs for Menu

def change_difficulty(d):
    print('Selected difficulty: {0}'.format(d))
    DIFFICULTY[0] = d

def mainmenu_background():

    main_window.fill((40, 0, 40))

# -----------------------------------------------------------------------------

# PLAY MENU
play_menu = pygameMenu.Menu(main_window,
                            bgfun=mainmenu_background,
                            color_selected=(0,0,0),
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=(255, 255, 255),
                            font_size=30,
                            menu_alpha=100,
                            menu_color=(228, 55, 36),
                            menu_height=int(height_window * 0.6),
                            menu_width=int(width_window * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Play menu',
                            window_height=height_window,
                            window_width=width_window
                            )

play_menu.add_option('Start', maingame, DIFFICULTY,)
play_menu.add_selector('Select difficulty', [('Easy', 'EASY'),
                                             ('Medium', 'MEDIUM'),
                                             ('Hard', 'HARD'),
                                             ('very hard',"VERY HARD")],
                       onreturn=None,
                       onchange=change_difficulty)
play_menu.add_option('Return to main menu', PYGAME_MENU_BACK)


# About_menu

about_menu = pygameMenu.TextMenu(main_window,
                                 bgfun=mainmenu_background,
                                 color_selected=(0,0,0),
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=(255,255,255),
                                 # font_size_title=30,
                                 # font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=(228, 55, 36),
                                 menu_color_title=(0,0,0),
                                 menu_height=int(height_window * 0.6),
                                 menu_width=int(width_window * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=(255,255,255),
                                 text_fontsize=20,
                                 title='About',
                                 window_height=height_window,
                                 window_width=width_window
                                 )
for m in ABOUT:
    about_menu.add_line(m)
about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
about_menu.add_option('Return to menu', PYGAME_MENU_BACK)

# HELP

help_menu = pygameMenu.TextMenu(main_window,
                                 dopause = True,
                                 bgfun = mainmenu_background,
                                 color_selected =(0, 0, 0),
                                 font = pygameMenu.fonts.FONT_BEBAS,
                                 font_color =(255, 255, 255),
                                 # font_size_title = 30,
                                 # font_title = pygameMenu.fonts.FONT_8BIT,
                                 menu_color=(228, 55, 36),
                                 menu_color_title=(0, 0, 0),
                                 menu_height=int(height_window * 0.6),
                                 menu_width=int(width_window * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=(255, 255, 255),
                                 text_fontsize=20,
                                 title='help',
                                 window_height=height_window,
                                 window_width=width_window
                                 )

for m in HELP:
    help_menu.add_line(m)
help_menu.add_option("Return to menu", PYGAME_MENU_BACK)

# MainMenu

main_menu = pygameMenu.Menu(main_window,
                            window_width=width_window,
                            window_height=height_window,
                            font=pygameMenu.fonts.FONT_NEVIS,
                            title='Main Menu',
                            bgfun=mainmenu_background,
                            menu_color_title=(0, 0, 0),
                            menu_color=(228, 55, 36),
                            menu_height=int(height_window * 0.6),
                            menu_width=int(width_window * 0.6),
                            enabled = True,
                            menu_alpha = 90,
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False
                            )

main_menu.add_option('Play', play_menu, DIFFICULTY)
main_menu.add_option('Help', help_menu)
main_menu.add_option('About', about_menu)
main_menu.add_option(element_name='Exit',
                     element=PYGAME_MENU_EXIT)


# -----------------------------------------------------------------------------


while False == False:
    clock.tick(60)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                main_menu.enable()

    main_menu.mainloop(events)

    pygame.display.flip()
