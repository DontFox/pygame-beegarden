import pygame
from pygame.locals import *

import pygameMenu
from pygameMenu.locals import *

# -------------------------------------------------------------------------------------

window_width = 600
window_height = 500
COLOR_BACKGROUND = [128, 0, 128]
FPS = 60
H_SIZE = 600  # Height of window size
W_SIZE = 800  # Width of window size


# ------------------------------------------------------------------------------------

pygame.init()


win = pygame.display.set_mode((W_SIZE, H_SIZE)
                              )

clock = pygame.time.Clock()

# -------------------------------------------------------------------------------------

def mainmenu_background():

    win.fill((40, 0, 40))
def pos1():
    None

# -------------------------------------------------------------------------------------

main_menu = pygameMenu.Menu(win,
                            bgfun = mainmenu_background,
                            enabled = True,
                            menu_alpha = 90,
                            title = 'Main Menu',
                            title_offsety = 5,

                            font = pygameMenu.fonts.FONT_NEVIS,

                            menu_color_title = (0, 0, 0),

                            window_width = W_SIZE,
                            window_height = H_SIZE
                            )

main_menu.add_option(element_name = 'Play',
                     element = pos1,
                     )
main_menu.add_option(element_name = 'Help',
                     element = pos1)

# menu = pygameMenu.Menu(surface,
#                        bgfun=mainmenu_background,
#                        enabled=False,
#                        font=pygameMenu.fonts.FONT_NEVIS,
#                        menu_alpha=90,
#                        onclose=PYGAME_MENU_CLOSE,
#                        title='Main Menu',
#                        title_offsety=5,
#                        window_height=H_SIZE,
#                        window_width=W_SIZE
#                        )

while 1:
    clock.tick(60)

    win.fill(COLOR_BACKGROUND)

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            exit()

    main_menu.mainloop(events)

    pygame.display.update()