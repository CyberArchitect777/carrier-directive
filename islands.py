
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
    
    def does_location_contain_island(self, x_pos, y_pos):
        """
        Iterates through all islands looking to see if any of them can be found at the passed location
        """
        for island in self.islands_list:
            if island.does_island_exist_here(x_pos, y_pos) == True:
                return True
        return False
    
    def is_location_near_island(self, x_pos, y_pos):
        """
        Checks to see if the provided location is nearby any island
        """
        for island in self.islands_list:
            if island.does_island_exist_in_next_square(x_pos, y_pos) == True:
                return True
        return False

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
