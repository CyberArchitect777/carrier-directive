
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
        self.turn_counter = 0
        self.map_data = map_data
        self.islands_data = map_data.return_islands_object()
        self.player_carrier = map_data.return_carrier(0)
        self.enemy_carrier = map_data.return_carrier(1)
        possible_directions = [ "n", "ne", "e", "se", "s", "sw", "w", "nw" ]
        print("\nWelcome to Carrier Directive")
        print("By Barrie Millar")
        print("A text-mode strategic game inspired by the 1988 game Carrier Command")
        print("\nDebug mode enabled by default")
        while (exitFlag == False):
            if self.turn_counter == 0:
                self.carrier_scan()
                self.turn_counter += 1
            print ("Turn " + str(self.turn_counter))
            print('Please enter a command or "h" for more information: ')
            command = input()
            if command.lower() == "h":
                print("\nCommands available\n")
                print("Game commands:\n")
                print("n ne e se s sw w nw - Move carrier in respective compass directions")
                print("status - Carrier status:")
                print("scan - Scan local area")
                print("is - Launches an aircraft to scout the nearby island")
                print("quit - Quits the game")
                print("\nDebug commands:\n")
                print("lp - Show location for the player carrier")
                print("le - Show location for the enemy carrier")
                print("m0 - Save a basic island map to basicmap.txt")
                print("m1 - Save an island ID linked map to islandmap.txt")
                print("m2 - Save a basic island (with feature map) to islandfeaturemap.txt")
                print("m3 - Save all maps available")
                print("pm - Moves the player carrier to the location specified\n")
            elif command.lower() == "quit":
                break
            elif command.lower() == "status":
                self.player_carrier = map_data.return_carrier(0)
                print("\nCarrier Status\n")
                print("Fuel: " + str(self.player_carrier.fuel))
                print("Supplies: " + str(self.player_carrier.supplies))
                print("Damage: " + str(self.player_carrier.damage) + "\n")
            elif command.lower() == "scan":
                self.carrier_scan()
            elif command.lower() == "is":
                nearby_islands = self.get_islands_near_carrier()
                if len(nearby_islands) > 1:
                    print("\nThe following island numbers are in range, please select which one you want to scout: ")
                    for current_island in nearby_islands:
                        print("\n" + current_island.island_id)
                    target_island = input()
                    while target_island not in nearby_islands:
                        print("\nThat island is not near your carrier, please try again:")
                        target_island = input()
                    self.player_carrier.launch_air_scout(self.islands_data.get_island_by_id(target_island))                       
                elif len(nearby_islands) == 1:
                    scout_result = self.player_carrier.launch_air_scout(nearby_islands[0])
                    if scout_result == 0:
                        print("\nYou have no aircraft available to scout this island.\n")
                    elif scout_result == 1:
                        print("\nYour air scout was unfortunately destroyed by defenses on the island. One aircraft was lost.\n")
                    else:
                        print("\nYour aircraft returned and you have data on the island available.\n")
                else:
                    print("\nThere are no islands near the carrier\n")
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
                print("Player Carrier Location - " + str(self.player_carrier.xlocation) + ", " + str(self.player_carrier.ylocation))
            elif command.lower() == "le":
                print("Enemy Carrier Location - " + str(self.enemy_carrier.xlocation) + ", " + str(self.enemy_carrier.ylocation))
            elif command.lower() == "pm":
                print("\nPlease enter a new X location for the player carrier:")
                new_x_pos = input()
                print("\nPlease enter a new Y location for the player carrier:")
                new_y_pos = input()
                validity_code = self.map_data.move_validity(int(new_x_pos), int(new_y_pos))
                if validity_code == 1:
                    self.carrier_scan()
                    print("\nInvalid location, out of the board!\n")
                elif validity_code == 2:
                    print("\nAn island is present here!\n")
                elif validity_code == 3:
                    print("\nThis is where the enemy carrier!\n")
                else:
                    self.player_carrier.xlocation = int(new_x_pos)
                    self.player_carrier.ylocation = int(new_y_pos)
                    self.carrier_scan()
            elif command.lower() in possible_directions:
                self.move_player_carrier(command.lower())
            else:
                print("\nCommand not recognised. Please try again.\n")

    def move_player_carrier(self, direction):
        next_xlocation = self.player_carrier.xlocation
        next_ylocation = self.player_carrier.ylocation
        if direction == "ne" or direction == "e" or direction == "se":
            next_xlocation += 1
        elif direction == "nw" or direction == "w" or direction == "sw":
            next_xlocation -= 1
        if direction == "ne" or direction == "n" or direction == "nw":
            next_ylocation -= 1
        if direction == "se" or direction == "s" or direction == "sw":
            next_ylocation += 1
        validity_code = self.map_data.move_validity(next_xlocation, next_ylocation)
        if validity_code == 1:
            self.carrier_scan()
            print("\nThis movement would take you out of the battle zone!\n")
        elif validity_code == 2:
            print("\nAn island is present here!\n")
        elif validity_code == 3:
            print("\nThis would ram the enemy carrier!\n")
        else:
            self.player_carrier.move_carrier(direction)
            self.turn_counter += 1
            self.carrier_scan()

    def get_islands_near_carrier(self):
        return self.islands_data.output_islands_near_location(self.map_data.return_carrier(0).xlocation, self.map_data.return_carrier(0).ylocation)

    def carrier_scan(self):
        print("\nCarrier Scan\n")
        print("Legend: C = Player Carrier, - = Water, I = Island, X = Out of Map Zone\n")
        islands_near_carrier = self.get_islands_near_carrier()
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
                    elif scanned_map[y][x] == -2:
                        print("E ", end="")
                    else:
                        print("I ", end="")
            print("\n")
