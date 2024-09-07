
from map import *
from user_interface import *

"""
    Main class for starting the game Carrier Directive.
"""

OCEANSIZE = 100 # Size of the game map
ISLANDS = 50 # Number of islands to be generated
ISLAND_MIN_SIZE = 2 # Minimum size of the island in both x and y directions
ISLAND_MAX_SIZE = 6 # Maximum size of the island in both x and y directions

new_game = Map(OCEANSIZE, ISLANDS, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE) # Start generating the game
game_interface = UserInterface() # Start the user interface
new_game.write_island_map(0) # Draws a basic island map to basicmap.txt
new_game.write_island_map(1) # Draws a island ID linked map to islandmap.txt
new_game.write_island_map(2) # Draws a basic island (with feature map) to islandfeaturemap.txt
