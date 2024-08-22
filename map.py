
import numpy
from islands import *

class Map():
    def __init__(self, OCEANSIZE, ISLANDS, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE):
        self.islands_list = Islands(OCEANSIZE, ISLANDS, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE)
        self.OCEANSIZE = OCEANSIZE
        
    def write_island_map(self, map_type):
        """
        Writes a selected ASCII-art map to a designated file according to the type of map needed.

        Parameters:

        map_type (int): The type of map needed as shown below. 0 is the assumed default for any other value:
            0 is a basic map, just showing islands and water
            1 shows the same, but each island is shown in a different character according to their island_id (up to 94 islands without repeating. Repeats occur after that.)
        """
        map_data = numpy.zeros((self.OCEANSIZE, self.OCEANSIZE))
        for island in self.islands_list.return_islands_list():
            island_full_coords = island.provide_coords()
            for island_coord in island_full_coords:
                xy_coords = island_coord.split(",")
                if map_type == 1:
                    map_data[int(xy_coords[0])][int(xy_coords[1])] = island.island_id
                else:
                    map_data[int(xy_coords[0])][int(xy_coords[1])] = 1
        if map_type == 1:
            map_file = open("islandmap.txt", "w")
        else:
            map_file = open("basicmap.txt", "w")
        for y in range(self.OCEANSIZE):
            for x in range(self.OCEANSIZE):
                if map_data[x][y] == 0:
                    map_file.write("-")
                else:
                    if map_type == 1:
                        character_number = (map_data[x][y] % 94) + 33
                        map_file.write(chr(int(character_number)))
                    else:
                        map_file.write("#")
            map_file.write("\n")
        map_file.close()