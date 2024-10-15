
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

class Feature():
    """
        Class representing an island feature
    """

    def __init__(self, x_location, y_location, feature_number):
        """
            Imports the required values for a fresh feature
        """
        self.x_location = x_location
        self.y_location = y_location
        self.feature_number = feature_number
        # Feature types specified by feature_number above
        # 2 - Command Center
        # 3 - Lasers Turret (powerful against aircraft and hovercrafts)
        # 4 - Anti-Aircraft guns (powerful against aircraft)
        # 5 - Rocket Launchers (powerful against hovercrafts)
        # 6 - Drone base
        # 7 - Radar systems
        # 8 - Fuel depot
        # 9 - Materials warehouse
