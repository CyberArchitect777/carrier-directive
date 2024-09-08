
class Carrier():
    """
        Class representing an aircraft carrier in the game.
    """

    def __init__(self, owner, xlocation, ylocation):
        """
        Sets up the required values for a fresh carrier and imports the owner ID in.
        """
        self.owner = owner
        self.xlocation = xlocation
        self.ylocation = ylocation
        self.damage = 0
        self.fuel = 100
        self.supplies = 100

    def return_carrier_location(self):
        """
        Return x and y locations of this carrier in two return parameters.
        """
        return self.xlocation, self.ylocation
