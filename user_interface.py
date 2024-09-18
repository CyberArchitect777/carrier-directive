
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
        turn_counter = 0
        self.map_data = map_data
        self.islands_data = map_data.return_islands_object()
        player_carrier = map_data.return_carrier(0)
        enemy_carrier = map_data.return_carrier(1)
        print("\nWelcome to Carrier Directive")
        print("By Barrie Millar")
        print("A text-mode strategic game inspired by the 1988 game Carrier Command")
        print("\nDebug mode enabled by default")
        while (exitFlag == False):
            if turn_counter == 0:
                self.carrier_scan()
                turn_counter += 1
            print ("Turn " + str(turn_counter))
            print('Please enter a command or "h" for more information: ')
            command = input()
            if command.lower() == "h":
                print("\nCommands available\n")
                print("Game commands:\n")
                print("n ne e se s sw w nw - Move carrier in respective compass directions")
                print("status - Carrier status:")
                print("scan - Scan local area")
                print("quit - Quits the game")
                print("\nDebug commands:\n")
                print("lp - Show location for the player carrier")
                print("le - Show location for the enemy carrier")
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
            elif command.lower() == "scan":
                self.carrier_scan()
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
            elif command.lower() == "lp":
                print("Player Carrier Location - " + str(player_carrier.xlocation) + ", " + str(player_carrier.ylocation))
            elif command.lower() == "le":
                print("Enemy Carrier Location - " + str(enemy_carrier.xlocation) + ", " + str(enemy_carrier.ylocation))
            elif command.lower() == "n":
                self.map_data.move_validity(player_carrier.xlocation, (player_carrier.ylocation-1))
                player_carrier.move_carrier("n")
                turn_counter += 1
                self.carrier_scan()
            elif command.lower() == "ne":
                self.map_data.move_validity((player_carrier.xlocation+1), (player_carrier.ylocation-1))
                player_carrier.move_carrier("ne")
                turn_counter += 1
                self.carrier_scan()
            elif command.lower() == "e":
                self.map_data.move_validity((player_carrier.xlocation+1), player_carrier.ylocation)
                player_carrier.move_carrier("e")
                turn_counter += 1
                self.carrier_scan()
            elif command.lower() == "se":
                self.map_data.move_validity((player_carrier.xlocation+1), (player_carrier.ylocation+1))
                player_carrier.move_carrier("se")
                turn_counter += 1
                self.carrier_scan()
            elif command.lower() == "s":
                self.map_data.move_validity(player_carrier.xlocation, (player_carrier.ylocation+1))
                player_carrier.move_carrier("s")
                turn_counter += 1
                self.carrier_scan()
            elif command.lower() == "sw":
                self.map_data.move_validity((player_carrier.xlocation-1), (player_carrier.ylocation+1))
                player_carrier.move_carrier("sw")
                turn_counter += 1
                self.carrier_scan()
            elif command.lower() == "w":
                self.map_data.move_validity((player_carrier.xlocation-1), player_carrier.ylocation)
                player_carrier.move_carrier("w")
                turn_counter += 1
                self.carrier_scan()
            elif command.lower() == "nw":
                self.map_data.move_validity((player_carrier.xlocation-1), (player_carrier.ylocation-1))
                player_carrier.move_carrier("nw")
                turn_counter += 1
                self.carrier_scan()
            else:
                print("\nCommand not recognised. Please try again.\n")

    

    def carrier_scan(self):
        print("\nCarrier Scan\n")
        print("Legend: C = Player Carrier, - = Water, I = Island, X = Out of Map Zone\n")
        islands_near_carrier = self.islands_data.output_islands_near_location(self.map_data.return_carrier(0).xlocation, self.map_data.return_carrier(0).ylocation)
        if len(islands_near_carrier) > 0:
            ISLAND_OWNER = [ "Unclaimed", "Player Claimed", "Enemy Claimed"]
            for island in islands_near_carrier:
                print("* Island " + str(island.island_id) + " (" + ISLAND_OWNER[island.island_owner] + ") is near the carrier\n")
        scan_radius = 3
        scanned_map = self.map_data.graphical_scan_from_carrier(self.map_data.return_carrier(0), scan_radius)
        # Create a array of the specified size full of empty strings
        map_graphical_data = numpy.full(((scan_radius * 2) + 1, (scan_radius * 2) + 1), "", dtype=str)
        for x in range((scan_radius * 2) + 1):
            for y in range((scan_radius * 2) + 1):
                if (x == scan_radius) and (y == scan_radius):
                    print("C ", end="")
                else:
                    if scanned_map[y][x] == 0:
                        print("- ", end="")
                    elif scanned_map[y][x] == -1:
                        print("X ", end="")
                    else:
                        print("I ", end="")
            print("\n")
