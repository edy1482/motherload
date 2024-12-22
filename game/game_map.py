# map.py has a class called map
# map builds a game map, with random ore placement according to levels
# The map is represented by a 2D list with each number representing a certain ore

import blocks

class game_map():
    """game_map"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0] * width for _ in range(height)] #initializes the map with 0s
        
    def build_map(self):
        for y in range(self.width):
            for x in range(self.height):
                self.map[x][y] = blocks.ore.Dirt
                
    def print(self):
        for row in self.map:
            print(row)
                



### TESTS ###

def main():
    test_map = game_map(30, 700)
    test_map.print()
    test_map.build_map()
    test_map.print()

if __name__ == "__main__":
    main()
    
    