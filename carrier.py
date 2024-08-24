
class Carrier():

    """
        Carrier is a class that contains the attributes and methods required to represent a carrier in the game.

        Attributes:
            owner (int): An integer representing the owner of the carrier
            xlocation (int): The X coordinate location of the carrier
            ylocation (int): The Y coordinate location of the carrier
            damage (int): The amount of damage the carrier has taken
            fuel (int): The fuel in percentage the carrier has left
            supplies (int): The current supply percentage of the carrier

        Method:

    """

    def __init__(self, owner):
        """
            Initalises the starting values of each carrier

            Arguments: 
                owner (int): Contains the owner of the carrier upon creation

        """
        self.owner = owner
        self.xlocation = -1
        self.ylocation = -1
        self.damage = 0
        self.fuel = 100
        self.supplies = 100
