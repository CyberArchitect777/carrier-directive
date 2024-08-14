
import numpy 
import random

OCEANSIZE = 100
ISLANDS = 50
ISLAND_MAX_SIZE = 5
ISLAND_MIN_SIZE = 1

def place_islands(oceanmap):
    for x in range(50):
        xlocation_center = random.randint(1,OCEANSIZE)
        ylocation_center = random.randint(1,OCEANSIZE)
        size = random.randint(1, 5)
        oceanmap[xlocation_center][ylocation_center] = 1
        if xlocation_center - size < 0:
            xlocation_start = 0
        else:
            xlocation_start - size
        if ylocation_center - size < 0:
            ylocation_start = 0
        else:
            ylocation_start - size
        for x in range(size):
            for y in range(size):
                oceanmap[xlocation_start+x][ylocation_start+y] = 1
    return oceanmap


def generate_empty_ocean_map():
    return numpy.zeros((OCEANSIZE, OCEANSIZE))

def main_game():
    oceanmap = generate_empty_ocean_map()
    place_islands(oceanmap)
