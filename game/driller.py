# driller.py has a class called driller, which is a sprite for the driller (aka the player)

import pygame

class driller(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)