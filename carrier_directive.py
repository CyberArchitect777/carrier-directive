
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
from user_interface import *

"""
    Main class for starting the game Carrier Directive.
"""

OCEANSIZE = 100 # Size of the game map
ISLANDS = 50 # Number of islands to be generated
ISLAND_MIN_SIZE = 2 # Minimum size of the island in both x and y directions
ISLAND_MAX_SIZE = 6 # Maximum size of the island in both x and y directions

new_map = Map(OCEANSIZE, ISLANDS, ISLAND_MIN_SIZE, ISLAND_MAX_SIZE) # Start generating the game
game_interface = UserInterface(new_map) # Start the user interface
