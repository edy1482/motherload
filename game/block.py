# block.py has a class called block, which is a sprite for dirt/ore blocks

import pygame
import os
from enum import Enum

class ore(Enum):
    Dirt = 0
    Copper = 1
    Iron = 2
    Silver = 3
    Gold = 4
    Platinum = 5
    Uranium = 6
    Palladium = 7
    Plutonium = 8
    Iridium = 9
    

class block(pygame.sprite.Sprite):
    # width and height are the dimensions of the block
    # id belongs to the ore class
    # multiplier multiplies the ore value
    # value is how much the ore can sell for in the shop
    def __init__(self, ore_id, x, y, width = 100, height = 100, multiplier = 1):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.ore_id = ore_id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.multiplier = multiplier
        
        # Derived variables
        self.ore_variables = self.assignments()
        self.value = self.ore_variables[0]
        self.img = pygame.image.load(os.path.join("../assets/blocks", self.ore_variables[1]))
        self.rect = self.img.get_rect()
        
    
    # assign initial values
    def assignments(self) -> tuple:
        match ore(self.ore_id):
            case ore.Dirt:
                return (0, "dirt.png")
            case ore.Copper:
                return (10, "copper.png")
            case ore.Iron:
                return (25, "iron.png")
            case ore.Silver:
                return (50, "silver.png")
            case ore.Gold:
                return (100, "gold.png")
            case ore.Platinum:
                return (500, "platinum.png")
            case ore.Uranium:
                return (1000, "uranium.png")
            case ore.Palladium:
                return (5000, "palladium.png")
            case ore.Plutonium:
                return (10000, "plutonium.png")
            case ore.Iridium:
                return (100000, "iridium.png")
    
    # public function for updating the value when multipliers change    
    def update_value(self):
        self.value = self.assign_value() * self.multiplier
        
    def print(self):
        print(f"ore_id: {self.ore_id}, value: {self.value}")
        

### TESTS ###

test_block = block(0, 0, 0)
test_block.print()
    

    


    