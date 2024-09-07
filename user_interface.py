
from map import *

class UserInterface():
    """
        Class representing the user interface in the game
    """

    def __init__(self, map_data):
        """
            Sets up the game loop that provides output and receives input from the user
        """
        exitFlag = False
        print("\nWelcome to Carrier Directive")
        print("By Barrie Millar")
        print("A text-mode strategic game inspired by the 1988 game Carrier Command")
        print("\nDebug mode enabled by default\n")
        while (exitFlag == False):
            print('Please enter a command or "h" for more information')
            command = input()
            if command.lower() == "h":
                print("\nCommands available\n")
                print("quit - Quits the game")
                print("m0 - Save a basic island map to basicmap.txt")
                print("m1 - Save an island ID linked map to islandmap.txt")
                print("m2 - Save a basic island (with feature map) to islandfeaturemap.txt")
                print("m3 - Save all maps available\n")
                print("s - Show status for the player carrier")
            elif command.lower() == "quit":
                break
            elif command.lower() == "m0":
                map_data.write_island_map(0) # Draws a basic island map to basicmap.txt
            elif command.lower() == "m1":
                map_data.write_island_map(1) # Draws a island ID linked map to islandmap.txt
            elif command.lower() == "m2":
                map_data.write_island_map(2) # Draws a basic island (with feature map) to islandfeaturemap.txt
            elif command.lower() == "m3":
                map_data.write_island_map(0) # Draws a basic island map to basicmap.txt
                map_data.write_island_map(1) # Draws a island ID linked map to islandmap.txt
                map_data.write_island_map(2) # Draws a basic island (with feature map) to islandfeaturemap.txt
            elif command.lower() == "s":
                map_data.carrier_list 
                print()

