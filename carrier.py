
import numpy 
import random

def place_islands(OCEANSIZE, ISLANDS, ISLANDS_MINSIZE, ISLANDS_MAXSIZE, oceanmap):
    for x in range(ISLANDS):
        xlocation_center = random.randint(0,OCEANSIZE-1)
        ylocation_center = random.randint(0,OCEANSIZE-1)
        size = random.randint(ISLANDS_MINSIZE, ISLANDS_MAXSIZE)
        oceanmap[xlocation_center][ylocation_center] = 1
        if xlocation_center - size < 0:
            xlocation_start = 0
        else:
            xlocation_start = xlocation_center - size
        if ylocation_center - size < 0:
            ylocation_start = 0
        else:
            ylocation_start = ylocation_center - size
        for x in range(size):
            for y in range(size):
                oceanmap[xlocation_start+x][ylocation_start+y] = 1
    return oceanmap


def write_human_map(oceanmap, filename, OCEANSIZE):
    map_file = open(filename, "w")
    for y in range(OCEANSIZE):
        for x in range(OCEANSIZE):
            if oceanmap[x][y] == 0:
                map_file.write("-")
            elif oceanmap[x][y] == 1:
                map_file.write("#")
        map_file.write("\n")
    map_file.close()

def generate_empty_ocean_map(OCEANSIZE):
    return numpy.zeros((OCEANSIZE, OCEANSIZE))

def main_game():
    OCEANSIZE = 100 # Size of the map
    ISLANDS = 50 # Number of islands
    ISLAND_MIN_SIZE = 1 # Island maximum size in pixels
    ISLAND_MAX_SIZE = 5 # Island maximum size in pixels
    oceanmap = generate_empty_ocean_map(OCEANSIZE)
    oceanmap = place_islands(OCEANSIZE, ISLANDS, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE, oceanmap)
    write_human_map(oceanmap, "oceanmap.txt", OCEANSIZE)

main_game() # Run main game function