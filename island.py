
import random

class Island():
    def __init__(self):
        self.island_owner = 0 # Island owner, 0 = Nobody, 1 = Player, 2 = AI
        # Starts with no information until generated
        self.island_id = -1
        self.xstartlocation = -1
        self.ystartlocation = -1
        self.size = -1

    def generate_random_island(self, island_number, OCEANSIZE, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE):
        flag = False
        self.size = random.randint(ISLAND_MIN_SIZE, ISLAND_MAX_SIZE)
        while (flag == False): # Generate the island coordinates until one is chosen that is within the map boundaries
            self.island_id = island_number
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