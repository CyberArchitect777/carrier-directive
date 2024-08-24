
from carrier import *

class Carriers():
    """
    Creates and manages a collection of all carriers in the game
    """
    def __init__(self):
        """
        Creates a fresh Carriers object and prepares a list to hold the collection of Carrier objects
        """
        self.carriers_list = [] # The carriers storage list

    def add_carrier(self, owner, xlocation, ylocation):
        """ 
        Add a fresh carrier object to the carriers list
        """
        self.carriers_list.append(Carrier(owner, xlocation, ylocation))
    