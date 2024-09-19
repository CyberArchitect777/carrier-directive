
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

    def return_islands_object(self):
        """
        Returns the islands object associated with this map
        """
        return self.islands_list

    def graphical_scan_from_carrier(self, carrier, scan_radius):
        """
        Returns a graphical representation of the immediate locality around the selected carrier
        """
        xposition, yposition = carrier.return_carrier_location()
        scan_size = (scan_radius * 2) + 1
        internal_map_data = numpy.zeros((int(scan_size), int(scan_size))) # Generate an empty list representing the immediate locality
        
        xstartposition = xposition - scan_radius
        ystartposition = yposition - scan_radius

        for island in self.islands_list.return_islands_list():
            for x in range(xstartposition, xstartposition + scan_size):
                for y in range(ystartposition, ystartposition + scan_size):
                    if x < 0 or y < 0 or x > (self.OCEANSIZE-1) or y > (self.OCEANSIZE-1):
                        internal_map_data[x-xstartposition][y-ystartposition] = -1
                    else:
                        if island.does_island_exist_here(x, y):
                            internal_map_data[x-xstartposition][y-ystartposition] = island.island_id
        
        return internal_map_data
    
    def move_validity(self, x_location, y_location):
        """
        Checks to see if there is any reason why a carrier cannot move to this location
        Returns the following code:
        0 = Move is valid
        1 = Move is off the edge of the map
        2 = Move is in an island
        3 = Move is into the space occupied by an enemy carrier
        """

        if x_location < 0 or y_location < 0 or x_location > (self.OCEANSIZE-1) or y_location > (self.OCEANSIZE-1):
            return 1
        elif self.islands_list.does_location_contain_island(x_location, y_location):
            return 2
        elif (self.carrier_list.return_carrier(1)).xlocation == x_location and (self.carrier_list.return_carrier(1)).ylocation == y_location:
            return 3
        else:
            return 0

    def return_carrier(self, carrier_number):
        """
        Returns a Carrier object based on the number provided by the user
        """
        return self.carrier_list.return_carrier(carrier_number)

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
            2 is the same map as 0 but with features mapped onto the island locations
        """

        map_data = numpy.zeros((self.OCEANSIZE, self.OCEANSIZE)) # Generate an empty list representing a map
        # Map symbols = HQ, Laser, Anti-Aircraft, Missile, Drone, Radar, Fuel, Warehouse
        MAP_SYMBOLS = [ "H", "L", "A", "M", "D", "R", "F", "W"] 
        for island in self.islands_list.return_islands_list():
            # For each island, fetch all the coordinates it occupies and write to the map_data list to highlight the
            # data that needs to be displayed.
            island_full_coords = island.provide_coords()
            for island_coord in island_full_coords:
                xy_coords = island_coord.split(",")
                if map_type == 1:
                    map_data[int(xy_coords[0])][int(xy_coords[1])] = island.island_id
                elif map_type == 0:
                    map_data[int(xy_coords[0])][int(xy_coords[1])] = 1
                elif map_type == 2:
                    if island.return_feature_value_by_coord(xy_coords[0], xy_coords[1]) == -1:
                        map_data[int(xy_coords[0])][int(xy_coords[1])] = 1
                    else:
                        map_data[int(xy_coords[0])][int(xy_coords[1])] = island.return_feature_value_by_coord(xy_coords[0], xy_coords[1])
            # Place -5 value for player carrier
            map_data[int(self.carrier_list.return_carrier(0).xlocation)][int(self.carrier_list.return_carrier(0).ylocation)] = -5
            # Place -10 value for enemy carrier
            map_data[int(self.carrier_list.return_carrier(1).xlocation)][int(self.carrier_list.return_carrier(1).ylocation)] = -10
        if map_type == 1:
            map_file = open("islandmap.txt", "w")
        elif map_type == 0:
            map_file = open("basicmap.txt", "w")
        elif map_type == 2:
            map_file = open("basicfeaturemap.txt", "w")
        for y in range(self.OCEANSIZE):
            for x in range(self.OCEANSIZE):
                if map_data[x][y] == 0:
                    map_file.write("-")
                elif map_data[x][y] == -5 and map_type == 0:
                    map_file.write("P")
                elif map_data[x][y] == -10 and map_type == 0:
                    map_file.write("E")
                elif map_data[x][y] > 1 and map_type == 2:
                    map_file.write(str(MAP_SYMBOLS[int(map_data[x][y])-2]))
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