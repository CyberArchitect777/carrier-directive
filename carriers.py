
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

from carrier import *

class Carriers():
    """
    Creates and manages a collection of all carriers in the game
    """
    def __init__(self):
        """
        Creates a fresh Carriers object and prepares a list to hold the collection of Carrier objects
        """
        self.carriers_list = [] # The carriers storage list

    def add_carrier(self, owner, xlocation, ylocation):
        """ 
        Add a fresh carrier object to the carriers list
        """
        self.carriers_list.append(Carrier(owner, xlocation, ylocation))

    def return_carrier(self, carrier_number):
        """
        Returns a single Carrier object by the specified carrier number
        """
        return self.carriers_list[carrier_number]
    