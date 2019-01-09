import pygame
pygame.init()
(width, height) = (720, 480)

screen = pygame.display.set_mode((width, height))
myfont = pygame.font.SysFont("monospace", 25)

clock = pygame.time.Clock()
minutes = 0
seconds = 0
milliseconds = 0

cover = pygame.Surface((160,35)).convert()
cover.fill((220, 220, 220))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if milliseconds > 1000:
        seconds += 1
        milliseconds -= 1000
        screen.blit(cover, (0,0))
        pygame.display.update()

    if seconds > 60:
        minutes += 1
        seconds -= 60
    milliseconds += clock.tick_busy_loop(60)
    timelabel = myfont.render("{}:{}".format(minutes, seconds), True, (0,0,0))
    screen.blit(timelabel,(0, 0))


    pygame.display.update()