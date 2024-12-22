# block.py has a class called block, which is a sprite for dirt/ore blocks
# read from a csv file to an object wrapper?

import pygame
import os
from enum import Enum

class ore(Enum):
    Dirt = 0
    Copper = 1
    Iron = 2
    Coal = 3
    Silver = 4
    Gold = 5
    Platinum = 6
    Uranium = 7
    Palladium = 8
    Plutonium = 9
    Iridium = 10
    

class block(pygame.sprite.Sprite):
    # id = block id (for iterating withing the Sprite Group)
    # ore_id = the ore type of the block (see ore class above)
    # x, y = the coord position of the block
    # width, height = the dimensions of the block
    # value_multiplier = the multiplier effect on the value (for upgrades later in game progression)
    # mining_multiplier = the multiplier effect on the mining speed of the block
    
    # value = how much the block sells for in the shop
    # mining_speed = how fast the driller sprite can mine the block
    # img = the png image used for the block
    # rect = the rectangular bounds used for the block (necessary for the Sprite class) 
    def __init__(self, id, ore_id, x, y, width = 100, height = 100, value_multiplier = 1, mining_multiplier = 1):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.ore_id = ore_id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value_multiplier = value_multiplier
        self.mining_multiplier = mining_multiplier
        
        # Derived variables
        self.ore_variables = self.assignments()
        self.value = self.ore_variables[0]
        self.mining_speed = self.ore_variables[1]
        self.img = pygame.image.load(os.path.join("../assets/blocks", self.ore_variables[2]))
        self.rect = self.img.get_rect()
        
    
    # assign initial values
    def assignments(self) -> tuple:
        match ore(self.ore_id):
            case ore.Dirt:
                return (0, 2, "dirt.png")
            case ore.Copper:
                return (10, 3, "copper.png")
            case ore.Iron:
                return (25, 5, "iron.png")
            case ore.Coal:
                return (50, 7, "coal.png")
            case ore.Silver:
                return (100, 11, "silver.png")
            case ore.Gold:
                return (500, 13, "gold.png")
            case ore.Platinum:
                return (1000, 17, "platinum.png")
            case ore.Uranium:
                return (5000, 19, "uranium.png")
            case ore.Palladium:
                return (10000, 23, "palladium.png")
            case ore.Plutonium:
                return (50000, 29, "plutonium.png")
            case ore.Iridium:
                return (100000, 31, "iridium.png")
    
    # function for updating the value when multipliers change    
    def update_assignments(self):
        self.value = self.ore_variables[0] * self.value_multiplier
        self.mining_speed = self.ore_variables[1] * self.mining_multiplier
        
    def print(self):
        print(f"ore_id: {self.ore_id}, mining_speed: {self.mining_speed}, value: {self.value}")
        

### TESTS ###

def main():
    return

if __name__ == "__main__":
    main()   


    