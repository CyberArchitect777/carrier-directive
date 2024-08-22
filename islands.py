
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
            if self.checkduplicate(current_island) == False: # Generate a new island until the coordinates are in empty map on the map
                self.islands_list.append(current_island)
                islandNumber += 1
                print("Generating island " + str(islandNumber))

    def checkduplicate(self, selected_island):
        """
        Checks the island passed in does not share duplicate coordinates with any other found in island storage list
        """
        for island in self.islands_list:
            if selected_island.contains_duplicate_coords(island):
                return True
        return False

    def return_islands_list(self):
        return self.islands_list
