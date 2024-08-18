
import numpy
from islands import *

class Map():
    def __init__(self, OCEANSIZE, ISLANDS, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE):
        self.islands_list = Islands(OCEANSIZE, ISLANDS, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE)
        print(self.islands_list.return_islands_list())
        self.OCEANSIZE = OCEANSIZE

    def write_basic_island_map(self):
        map_data = numpy.zeros((self.OCEANSIZE, self.OCEANSIZE))
        for island in self.islands_list.return_islands_list():
            island_full_coords = island.provide_coords()
            for island_coord in island_full_coords:
                xy_coords = island_coord.split(",")
                map_data[int(xy_coords[0])][int(xy_coords[1])] = 1
        map_file = open("basicmap.txt", "w")
        for y in range(self.OCEANSIZE):
            for x in range(self.OCEANSIZE):
                if map_data[x][y] == 0:
                    map_file.write("-")
                elif map_data[x][y] == 1:
                    map_file.write("#")
            map_file.write("\n")
        map_file.close()
