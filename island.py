
import random

class Island():
    def __init__(self):
        self.xstartlocation = 0;
        self.ystartlocation = 0;
        self.size = 0;

    def generate_random_island(self, OCEANSIZE, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE):
        flag = True
        self.size = random.randint(ISLAND_MIN_SIZE, ISLAND_MAX_SIZE)
        while (flag == False):
            self.xstartlocation = random.randint(0,OCEANSIZE-1)
            self.ystartlocation = random.randint(0,OCEANSIZE-1)
            if (self.xstartlocation + self.size) > OCEANSIZE:
                flag == False
            if (self.ystartlocation + self.size) > OCEANSIZE:
                flag == False
    
    def provide_coords(self):
        island_coords = []
        for y in range(self.size):
            for x in range(self.size):
                island_coords.append(str(self.xstartlocation) + "," + str(self.ystartlocation))
        return island_coords

    def contains_duplicate_coords(self, selected_island):
        if (list(set(selected_island.provide_coords()).intersection(self.provide_coords())) == ""):
            return False
        else:
            return True