
import random

class Island():
    """
    Class representing a single island in the game.
    
    """
    def __init__(self):
        """
        Sets up the variables on a new island with placeholder values.
        """
        self.island_owner = 0 # Island owner, 0 = Nobody, 1 = Player, 2 = AI
        # Starts with no information until generated
        self.island_id = -1
        self.xstartlocation = -1
        self.ystartlocation = -1
        self.size = -1
        self.features = []

    def generate_random_island(self, island_number, OCEANSIZE, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE):
        """
        Creates a random island and ensure it fits on the map
        """
        flag = False
        self.size = random.randint(ISLAND_MIN_SIZE, ISLAND_MAX_SIZE)
        while (flag == False): # Generate the island coordinates until one is chosen that is within the map boundaries
            self.island_id = island_number
            self.xstartlocation = random.randint(0,OCEANSIZE-1)
            self.ystartlocation = random.randint(0,OCEANSIZE-1)
            if (self.xstartlocation + self.size) < OCEANSIZE: # Checks to see if the generation does not go off the side of the map.
                if (self.ystartlocation + self.size) < OCEANSIZE:
                    print("Random island start x - " + str(self.xstartlocation))
                    print("Random island start y - " + str(self.ystartlocation))
                    print("Random island size = " + str(self.size))
                    flag = True
        # Determine how many features this island will have
        if (self.size < 9 ):
            feature_number = 2
        else:
            feature_number = int(self.size / 2) # Rounds down this number
        for feature_number in range(feature_number):
            select_feature = 5
            # Select a random feature to apply from the following
            # 0 - Lasers Turret (powerful against aircraft and hovercrafts)
            # 1 - Anti-Aircraft guns (powerful against aircraft)
            # 2 - Rocket Launchers (powerful against hovercrafts)
            # 3 - Drone base
            # 4 - Radar systems
            # 5 - Fuel depot
            # 6 - Materials warehouse
            # 7 - Command Center
            if (feature_number == 0):
                # Makes sure a command center is selected first
                select_feature = 7
            else:
                # Select any other feature if this is not the first feature
                select_feature = random.randint(0,6)
            island_coords = self.provide_coords()
            selected_island_location = random.randint(0, len(island_coords))
            self.features.append([ selected_island_location, select_feature ])

    def provide_coords(self):
        """
        Provide a total list of coordinates in which this island exists
        """
        island_coords = []
        for y in range(self.size):
            for x in range(self.size):
                island_coords.append(str(self.xstartlocation+x) + "," + str(self.ystartlocation+y))
        return island_coords
    
    def does_island_exist_here(self, x_pos, y_pos):
        """
        Checks to see if any part of the island exists at the provided coordinates
        """
        for location in self.provide_coords():
            x_location, y_location = location.split(",")
            if (x_pos == x_location) and (y_pos == y_location):
                return True
        return False

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
