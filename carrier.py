
from map import *

OCEANSIZE = 100 # Size of the game map
ISLANDS = 50 # Number of islands to be generated
ISLAND_MIN_SIZE = 2 # Minimum size of the island in both x and y directions
ISLAND_MAX_SIZE = 6 # Maximum size of the island in both x and y directions

new_game = Map(OCEANSIZE, ISLANDS, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE) # Start generating the game
new_game.write_basic_island_map() # Draws a basic island map to basicmap.txt
