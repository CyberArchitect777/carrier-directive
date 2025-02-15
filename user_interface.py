
"""
Carrier Directive: A text-mode strategic game inspired by the 1988 game Carrier Command
Copyright (C) 2024 Barrie Millar

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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
                print("Carrier commands:\n")
                print("n ne e se s sw w nw - Move carrier in respective compass directions")
                print("status - Carrier status")
                print("scan - Scan local area")
                print("\nIsland attack commands\n")
                print("is - Launches an aircraft to scout the nearby island")
                print("aa - Launches an aircraft attack on the nearby island")
                print("ga - Launches an hovercraft attack on the nearby island")
                print("\nGeneral game commands\n")
                print("quit - Quits the game")
                print("\nDebug commands for development:\n")
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
            elif command.lower() == "aa":
                # Launch an air attack on the island
                island_selected = self.determine_correct_nearby_island()
                if island_selected != None:
                    attack_direction = self.determine_attack_direction()
                    print("Attack direction" + attack_direction)
                    if attack_direction != None:
                        craft_status, attack_output = self.player_carrier.launch_attack(island_selected, attack_direction, True)
                        if craft_status == 0:
                            print("\nThere is no aircraft available for this attack")
                        elif craft_status == 1:
                            print("\n" + str(attack_output) + " defenses were destroyed. However, the aircraft was lost\n")
                        else:
                            print("\n" + str(attack_output) + " defenses were destroyed. The aircraft safely returned to the carrier\n")
                        if craft_status > 0:
                            print("Current island status:")
                            island_scan = island_selected.return_island_makeup_for_mapping()        
                            self.process_scout_result(2, island_scan, True)
            elif command.lower() == "ga":
                # Launch a ground attack on the island
                island_selected = self.determine_correct_nearby_island()
                if island_selected != None:
                    attack_direction = self.determine_attack_direction()
                    if attack_direction != None:
                        craft_status, attack_output = self.player_carrier.launch_attack(island_selected, attack_direction, False)
                        if craft_status == 0:
                            print("\nThere is no hovercraft available for this attack")
                        elif craft_status == 1:
                            print("\n" + str(attack_output) + " defenses were destroyed. However, the hovercraft was lost\n")
                        else:
                            print("\n" + str(attack_output) + " defenses were destroyed. The hovercraft safely returned to the carrier\n")
                        if craft_status > 0:
                            print("Current island status:\n")
                            island_scan = island_selected.return_island_makeup_for_mapping()        
                            self.process_scout_result(2, island_scan, True)
            elif command.lower() == "is":
                # Manage island scouting from the air
                island_selected = self.determine_correct_nearby_island()
                if island_selected != None:
                    scout_result = self.player_carrier.launch_air_scout(island_selected)
                    island_scan = island_selected.return_island_makeup_for_mapping()
                    self.process_scout_result(scout_result, island_scan, False)
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
            elif command.lower() == "lp": # Shows player carrier location for debugging
                print("Player Carrier Location - " + str(self.player_carrier.xlocation) + ", " + str(self.player_carrier.ylocation))
            elif command.lower() == "le": # Shows enemy carrier location for debugging
                print("Enemy Carrier Location - " + str(self.enemy_carrier.xlocation) + ", " + str(self.enemy_carrier.ylocation))
            elif command.lower() == "pm": # Allows the player carrier to be moved anywhere for debugging
                print("\nPlease enter a new X location for the player carrier:")
                new_x_pos = input()
                print("\nPlease enter a new Y location for the player carrier:")
                new_y_pos = input()
                validity_code = self.map_data.move_validity(int(new_x_pos), int(new_y_pos))
                # Checks to see if the new carrier location is valid
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
            elif command.lower() in possible_directions: # Moves the carrier in the compass direction specified
                self.move_player_carrier(command.lower())
            else: # Catch-all for invalid command
                print("\nCommand not recognised. Please try again.\n")

    def determine_attack_direction(self):
        """
        Determine which compass direction is used for an air or ground attack.
        N, S, E, W are acceptable values for returning
        """
        print("\nWhich direction do you want to launch the attack from")
        print("\nNorth, South, East or West (N, S, E, W):")
        direction = input()
        correct_selections = [ "north", "south", "east", "west", "n", "s", "e", "w"]
        if direction.lower() in correct_selections:
            return direction[0].lower()
        else:
            print("\n\nThat is an invalid direction, please try again.")
            return None        

    def determine_correct_nearby_island(self):
        """
        Determines which island the user wants to scout/attack.
        Returns the apropriate island to the calling code or None if the user specifies an invalid island
        """        
        nearby_island_ids = self.player_carrier.get_island_ids_near_carrier(self.islands_data)
        island_selected = None
        if len(nearby_island_ids) > 1: # If more than one island is detected
            print("\nThe following island numbers are in range:-\n")
            for current_island_id in nearby_island_ids:
                print(str(current_island_id))
            print("\nPlease select which one you want to scout: ")
            target_island = input()
            if int(target_island) in nearby_island_ids:
                island_selected = self.islands_data.return_island_by_id(int(target_island))
            else: # Output if user specifies an island not in range
                island_selected = None
            if island_selected == None: # Output if user specifies an island not in range
                print("\nThat island is not near your carrier, please try again:\n")
        elif len(nearby_island_ids) == 1: # Scouts the island if only one is in range
            island_selected = self.islands_data.return_island_by_id(nearby_island_ids[0])
        else: # Output if no islands are in range
            island_selected = None
            print("\nThere are no islands near the carrier\n")
        return island_selected

    def process_scout_result(self, scout_result, island_data, automatic):
        """
        Provides user output depending on the result of the island scout operation

        Automatic = Determines if this is a real scout from a user command or one #
        with details after a direct attack
        """        
        if scout_result == 0 and automatic == False:
            print("\nYou have no aircraft available to scout this island.\n")
        elif scout_result == 1 and automatic == False:
            print("\nYour air scout was unfortunately destroyed by defenses on the island. One aircraft was lost.\n")
        else:
            if automatic == False:
                print("\nYour aircraft returned and you have data on the island available.\n")
            print("\nLegend: - = Empty Island Space, C = Command Center, T = Laser Turret, A = Anti-Aircraft Guns")
            print("        L = Rocket Launchers, D = Drone Base, R = Radar Systems, F = Fuel Depot, W = Materials Warehouse\n")
            for x in range(len(island_data[0])):
                for y in range(len(island_data[0])):
                    if island_data[y][x] == 0:
                        print("- ", end="")
                    if island_data[y][x] == 2:
                        print("C ", end="")
                    if island_data[y][x] == 3:
                        print("T ", end="")
                    if island_data[y][x] == 4:
                        print("A ", end="")
                    if island_data[y][x] == 5:
                        print("L ", end="")
                    if island_data[y][x] == 6:
                        print("D ", end="")
                    if island_data[y][x] == 7:
                        print("R ", end="")
                    if island_data[y][x] == 8:
                        print("F ", end="")
                    if island_data[y][x] == 9:
                        print("W ", end="")                    
                print("\n")

    def move_player_carrier(self, direction):
        """
        Handles the interface manipulation of the player carrier by normal compass means
        """
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
        # Checks if the new location is valid for the carrier
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
            self.player_carrier.fuel -= 1
            self.carrier_scan()

    def carrier_scan(self):
        """
        Provides a user interface scan output for the area around the carrier        
        """
        print("\nCarrier Scan\n")
        print("Legend: C = Player Carrier, - = Water, I = Island, X = Out of Map Zone\n")
        # Identifies the islands next to the carrier location
        islands_near_carrier = self.player_carrier.get_islands_near_carrier(self.islands_data)
        if len(islands_near_carrier) > 0:
            ISLAND_OWNER = [ "Unclaimed", "Player Claimed", "Enemy Claimed"]
            for island in islands_near_carrier:
                print("* Island " + str(island.island_id) + " (" + ISLAND_OWNER[island.island_owner] + ") is near the carrier\n")
        scan_radius = 3
        scanned_map = self.map_data.graphical_scan_from_carrier(self.map_data.return_carrier(0), scan_radius)
        # Create a array of the specified size full of empty strings
        map_graphical_data = numpy.full(((scan_radius * 2) + 1, (scan_radius * 2) + 1), "", dtype=str)
        # Draws a map of the current scan radius with the carrier in the middle
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
