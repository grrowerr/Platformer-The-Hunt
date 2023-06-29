import pygame, sys
from main_settings import *
from level import  Level

pygame.init()
main_win = pygame.display.set_mode((scr_width, scr_height))
clock = pygame.time.Clock()
level = Level(level_map, main_win)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main_win.fill('black')
    level.run_level()

    pygame.display.update()
    clock.tick(60)
