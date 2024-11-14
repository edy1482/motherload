# map.py has a class called map
# map builds a game map, with random ore placement according to levels
# The map is represented by a 2D list with each number representing a certain ore

import block

class game_map():
    """game_map"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0] * width for _ in range(height)]
        
    def print(self):
        for row in self.map:
            print(row)
                



# TESTING

def main():
    test_map = game_map(5, 10)
    test_map.print()
    print(block.ore(0))

if __name__ == "__main__":
    main()
    
    