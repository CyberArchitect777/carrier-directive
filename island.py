
import random

class Island():
    def __init__(self):
        self.xstartlocation = 0
        self.ystartlocation = 0
        self.size = 0

    def generate_random_island(self, OCEANSIZE, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE):
        flag = False
        self.size = random.randint(ISLAND_MIN_SIZE, ISLAND_MAX_SIZE)
        while (flag == False): # Generate the island coordinates until one is chosen that is within the map boundaries
            self.xstartlocation = random.randint(0,OCEANSIZE-1)
            self.ystartlocation = random.randint(0,OCEANSIZE-1)
            if (self.xstartlocation + self.size) < OCEANSIZE:
                if (self.ystartlocation + self.size) < OCEANSIZE:
                    print("Random island start x - " + str(self.xstartlocation))
                    print("Random island start y - " + str(self.ystartlocation))
                    print("Random island size = " + str(self.size))
                    flag = True
    
    def provide_coords(self):
        """
        Provide a total list of coordinates in which this island exists
        """
        island_coords = []
        for y in range(self.size):
            for x in range(self.size):
                island_coords.append(str(self.xstartlocation+x) + "," + str(self.ystartlocation+y))
        return island_coords

    def contains_duplicate_coords(self, selected_island):
        """
        Compare another island to this one to see if any coordinates are shared
        """
        compare_island_space = set(selected_island.provide_coords()).intersection(self.provide_coords())
        print("Set length: " + str(len(compare_island_space)))
        if len(compare_island_space) == 0:
            return False
        else:
            return True