
from island import *

class Islands():
    def __init__(self, OCEANSIZE, ISLANDS, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE):
        self.islands_list = []

        islandNumber = 0

        while islandNumber < ISLANDS:
            current_island = Island()
            current_island.generate_random_island(OCEANSIZE, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE)
            if self.checkduplicate(current_island) == False:
                self.islands_list.append(current_island)
                islandNumber += 1
                print("Generating island " + str(islandNumber))

    def checkduplicate(self, selected_island):
        for island in self.islands_list:
            if selected_island.contains_duplicate_coords(island):
                return True
        return False

    def return_islands_list(self):
        return self.islands_list
