
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

from island import *

class Islands():
    """
    Creates and manages a collection of all islands in the game
    """
    def __init__(self, OCEANSIZE, ISLANDS, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE):
        self.islands_list = [] # The islands storage list

        islandNumber = 0

        while islandNumber < ISLANDS:
            current_island = Island()
            current_island.generate_random_island(islandNumber, OCEANSIZE, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE)
            if self.checkduplicate(current_island) == False: # Generates a new island constantly until the coordinates are in an empty area on the map
                self.islands_list.append(current_island)
                islandNumber += 1

    def checkduplicate(self, selected_island):
        """
        Checks the island passed in does not share duplicate coordinates with any other found in island storage list
        """
        for island in self.islands_list:
            if selected_island.contains_duplicate_coords(island):
                return True
        return False
    
    def return_island_by_id(self, island_number):
        """
        Returns an individual island if it matches the specified ID. Returns None if no island of that ID can be found
        """
        for island in self.islands_list:
            if island.island_id == island_number:
                return island
        return None
    
    def does_location_contain_island(self, x_pos, y_pos):
        """
        Iterates through all islands looking to see if any of them can be found at the passed location
        """
        for island in self.islands_list:
            if island.does_island_exist_here(x_pos, y_pos) == True:
                return True
        return False
    
    def output_islands_near_location(self, x_pos, y_pos, ids_only):
        """
        Output a list of all islands near the provided location

        ids_only:

        false - Provide full island objects
        true - Provide island ID's only
        """
        island_list = []
        for island in self.islands_list:
            if island.does_island_exist_in_next_square(x_pos, y_pos) == True:
                if (ids_only == True):
                    island_list.append(island.island_id)
                else:
                    island_list.append(island)
        return island_list
    
    def return_islands_list(self):
        """
        Returns the full list of island objects
        """
        return self.islands_list
    
    def return_number_of_islands(self):
        """
        Return the number of islands
        """
        return len(self.islands_list)
