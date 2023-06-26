import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((153, 245, 255))
        self.rect = self.image.get_rect(topleft= position)
