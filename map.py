
import numpy, random
from islands import *
from carriers import *

class Map():
    def __init__(self, OCEANSIZE, ISLANDS, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE):
        # Creates an islands object and assigns it to the value below
        self.islands_list = Islands(OCEANSIZE, ISLANDS, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE)
        self.OCEANSIZE = OCEANSIZE
        # Creates a player and enemy carrier object. Owner values are hardcoded for the moment as multiple carriers
        # are not scheduled for implementation from the beginning.
        self.carrier_list = Carriers()
        player_x_location, player_y_location = self.find_empty_location(OCEANSIZE)
        enemy_x_location, enemy_y_location = self.find_empty_location(OCEANSIZE)
        self.carrier_list.add_carrier(0, player_x_location, player_y_location)
        self.carrier_list.add_carrier(1, enemy_x_location, enemy_y_location)

    def find_empty_location(self, OCEANSIZE):
        """
        Finds an empty location on the map devoid of islands and returns it.
        """
        flag = False
        while (flag == False): # Generate the island coordinates until one is chosen that is within the map boundaries
            xlocation = random.randint(0,OCEANSIZE-1)
            ylocation = random.randint(0,OCEANSIZE-1)
            if self.islands_list.does_location_contain_island(xlocation, ylocation) == False:
                return xlocation, ylocation
        
    def write_island_map(self, map_type):
        """
        Writes a selected ASCII-art map to a designated file according to the type of map needed.

        map_type (int): The type of map needed as shown below. 0 is the assumed default for any other value:
            0 is a basic map, just showing islands and water
            1 shows the same, but each island is shown in a different character according to their island_id 
            (up to 94 islands without repeating. Repeats occur after that.)
        """
        map_data = numpy.zeros((self.OCEANSIZE, self.OCEANSIZE)) # Generate an empty list representing a map
        for island in self.islands_list.return_islands_list():
            # For each island, fetch all the coordinates it occupies and write to the map_data list to highlight the
            # data that needs to be displayed.
            island_full_coords = island.provide_coords()
            for island_coord in island_full_coords:
                xy_coords = island_coord.split(",")
                if map_type == 1:
                    map_data[int(xy_coords[0])][int(xy_coords[1])] = island.island_id
                else:
                    map_data[int(xy_coords[0])][int(xy_coords[1])] = 1
            # Place -5 value for player carrier
            map_data[int(self.carrier_list.return_carrier(0).xlocation)][int(self.carrier_list.return_carrier(0).ylocation)] = -5
            # Place -10 value for enemy carrier
            map_data[int(self.carrier_list.return_carrier(1).xlocation)][int(self.carrier_list.return_carrier(1).ylocation)] = -10
        if map_type == 1:
            map_file = open("islandmap.txt", "w")
        else:
            map_file = open("basicmap.txt", "w")
        for y in range(self.OCEANSIZE):
            for x in range(self.OCEANSIZE):
                if map_data[x][y] == 0:
                    map_file.write("-")
                elif map_data[x][y] == -5 and map_type == 0:
                    map_file.write("P")
                elif map_data[x][y] == -10 and map_type == 0:
                    map_file.write("E")
                else:
                    if map_type == 1:
                        # If each island needs a different character display, output a different ASCII character
                        # for each island ID
                        character_number = (map_data[x][y] % 94) + 33
                        map_file.write(chr(int(character_number)))
                    else:
                        map_file.write("#")
            map_file.write("\n")
        map_file.close()