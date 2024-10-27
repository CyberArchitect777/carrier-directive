
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

import random

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
        self.aircraft = 4
        self.hovercraft = 4

    def return_carrier_location(self):
        """
        Return x and y locations of this carrier in two return parameters.
        """
        return self.xlocation, self.ylocation
    
    def launch_air_scout(self, island):
        """
        The carrier launches an air scout to an island in order to view the facilities and defenses on it
        The following return codes might be used:
        0 = No aircraft available for this
        1 = Aircraft lost
        2 = Aircraft succeeded, scouting information available.
        """
        if self.aircraft < 1:
            return 0
        else:
            laser_turrents = island.return_number_features_by_type(3)
            aa_guns = island.return_number_features_by_type(4)
            drone_bases = island.return_number_features_by_type(6)
            risk_of_loss = (laser_turrents * 3) + (aa_guns * 10) + (drone_bases * 3)
            random_number = random.randint(0,99)
            if risk_of_loss >= random_number:
                self.aircraft -= 1
                return 1
            else:
                return 2
            
    def launch_air_attack(self, island, direction):
        """
        The carrier launches an air attack on the island from the direction specified.
        The directions can be one of: n, s, w, e
        The following return codes might be used:
        0 = No aircraft available for this
        1 = Aircraft lost
        2 = Aircraft succeeded, scouting information available.
        """
        if self.aircraft < 1:
            return 0
        else:
            island.island_attack(direction)
    
    def move_carrier(self, direction):
        """
        Move the carrier in a direction specified by a string based on abbreviated compass directions
        """
        if direction == "n":
            self.ylocation -= 1
        elif direction == "ne":
            self.xlocation += 1
            self.ylocation -= 1        
        elif direction == "e":
            self.xlocation += 1
        elif direction == "se":
            self.xlocation += 1
            self.ylocation += 1        
        elif direction == "s":
            self.ylocation += 1        
        elif direction == "sw":
            self.ylocation += 1
            self.xlocation -+ 1        
        elif direction == "w":
            self.xlocation -= 1
        elif direction == "nw":
            self.xlocation -= 1
            self.ylocation -= 1
