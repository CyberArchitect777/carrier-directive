
class Carrier():
    """
        Class representing an aircraft carrier in the game.
    """

    def __init__(self, owner):
        """
            Sets up the required values for a fresh carrier and imports the owner ID in.
        """
        self.owner = owner
        self.xlocation = -1
        self.ylocation = -1
        self.damage = 0
        self.fuel = 100
        self.supplies = 100
