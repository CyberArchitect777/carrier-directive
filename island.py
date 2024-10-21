
"""
Carrier Directive: A text-mode strategic game inspired by the 1988 game Carrier Command
Copyright (C) 2024 Barrie Millar

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import numpy, random
from features import *

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
        self.features = Features()

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
                    flag = True
        # Determine how many features this island will have
        if ((self.size ** 2) < 9 ):
            feature_number = 2
        else:
            feature_number = int((self.size ** 2) / 4) # Rounds down this number
        for current_feature_number in range(feature_number):
            # Select a random feature to apply from the following
            # 2 - Command Center
            # 3 - Lasers Turret (powerful against aircraft and hovercrafts)
            # 4 - Anti-Aircraft guns (powerful against aircraft)
            # 5 - Rocket Launchers (powerful against hovercrafts)
            # 6 - Drone base
            # 7 - Radar systems
            # 8 - Fuel depot
            # 9 - Materials warehouse
            if (current_feature_number == 0):
                # Makes sure a command center is selected first
                select_feature = 2
            else:
                # Select any other feature if this is not the first feature
                select_feature = random.randint(3,9)
                if (select_feature > 5):
                    flag = False
                    while (flag == False):
                        select_feature = random.randint(3,9)
                        if (select_feature < 6) and (select_feature > 2):
                            flag = True
                        elif (select_feature > 5):
                            if not self.features.does_feature_type_already_exist(select_feature):
                                flag = True              
            island_coords = self.provide_coords()
            selected_island_location = random.randint(0, len(island_coords)-1)
            selected_xy_coords = island_coords[selected_island_location].split(",")
            self.features.add_feature(selected_xy_coords[0], selected_xy_coords[1], select_feature)

    def return_island_makeup_for_mapping(self):
        """
        Return the makeup of the island including all features
        """
        island_map = numpy.zeros((int(self.size), int(self.size))) # Generate an empty island map
        featurelist = self.features.return_list_of_all_feature_objects()
        for feature in featurelist:
            relative_x, relative_y = feature.return_relative_island_location(self.xstartlocation, self.ystartlocation)
            island_map[relative_x][relative_y] = feature.feature_number
        return island_map

    def return_feature_value_by_coord(self, x_location, y_location):
        """
        Return feature value on the island by coordinates
        """

        return self.features.return_feature_value_by_coords(x_location, y_location)
    
    def return_number_features_by_type(self, feature_type):
        """
        Returns count of the number of features found on this island with the type specified
        """
        return self.features.count_number_of_individual_features_by_type(feature_type)

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
            if (x_pos == int(x_location)) and (y_pos == int(y_location)):
                return True
        return False
    
    def does_island_exist_in_next_square(self, x_pos, y_pos):
        """
        Checks to see if any part of the island exists in the next square to the provided coordinates
        """
        for location in self.provide_coords():
            x_location, y_location = location.split(",")
            for x_scan in range(-1, 2): # Starts loop at -1
                for y_scan in range(-1, 2):
                    if (x_pos == int(x_location)+x_scan) and (y_pos == int(y_location)+y_scan):
                        return True
        return False

    def contains_duplicate_coords(self, selected_island):
        """
        Compare another island to this one to see if any coordinates are shared
        """
        compare_island_space = set(selected_island.provide_coords()).intersection(self.provide_coords())
        if len(compare_island_space) == 0:
            return False
        else:
            return True
