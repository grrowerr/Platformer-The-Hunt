import pygame, sys
from main_settings import *
from tiles import Tile

pygame.init()
main_win = pygame.display.set_mode((scr_width, scr_height))
clock = pygame.time.Clock()
test_tile = pygame.sprite.Group(Tile((100, 100), 200)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main_win.fill('black')
    test_tile.draw(main_win)

    pygame.display.update()
    clock.tick(60)
