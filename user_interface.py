
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
                print("Game commands:\n")
                print("status - Carrier status:")
                print("quit - Quits the game")
                print("\nDebug commands:\n")
                print("p - Show location for the player carrier")
                print("e - Show location for the enemy carrier")
                print("m0 - Save a basic island map to basicmap.txt")
                print("m1 - Save an island ID linked map to islandmap.txt")
                print("m2 - Save a basic island (with feature map) to islandfeaturemap.txt")
                print("m3 - Save all maps available\n")
            elif command.lower() == "quit":
                break
            elif command.lower() == "status":
                player_carrier = map_data.return_carrier(0)
                print("\nCarrier Status\n")
                print("Fuel: " + str(player_carrier.fuel))
                print("Supplies: " + str(player_carrier.supplies))
                print("Damage: " + str(player_carrier.damage) + "\n")
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
            elif command.lower() == "p":
                player_carrier = map_data.return_carrier(0)
                print("Player Carrier Location - " + str(player_carrier.xlocation) + ", " + str(player_carrier.ylocation))
            elif command.lower() == "e":
                enemy_carrier = map_data.return_carrier(1)
                print("Enemy Carrier Location - " + str(enemy_carrier.xlocation) + ", " + str(enemy_carrier.ylocation))
            else:
                print("\nCommand not recognised. Please try again.\n")
