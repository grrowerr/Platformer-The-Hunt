import pygame
from tiles import Tile
from main_settings import tile_size, scr_width
from player import Player

class Level:
    def __init__(self, level_data, surface):

        #level setup
        self.display_surface = surface
        self.setup_level_tile(level_data)
        self.world_shift = 0

    def setup_level_tile(self, level_layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(level_layout):
            for col_index, column in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if column == 'X':
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                elif column == 'P':
                    main_player_sprite = Player((x,y))
                    self.player.add(main_player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < scr_width / 4 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        elif player_x > scr_width - (scr_width / 4) and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 5


    def run_level(self):
        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        #self player
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()