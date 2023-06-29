import pygame
from tiles import Tile
from main_settings import tile_size

class Level:
    def __init__(self, level_data, surface):

        #level setup
        self.display_surface = surface
        self.setup_level_tile(level_data)
        self.world_shift = 0

    def setup_level_tile(self, level_layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(level_layout):
            for col_index, column in enumerate(row):
                if column == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)


    def run_level(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)