import pygame # type: ignore
from settings import *
from tile import Tile


class Level:
    def __init__(self):

        # Sprites
        self.visible_sprites = pygame.sprite.Group()
        
        # Sprite setup
        self.create_map()
    
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,])

    def run(self,screen):
        
        self.visible_sprites.update()

        self.visible_sprites.draw(screen)
