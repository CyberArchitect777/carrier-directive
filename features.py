
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

from feature import *

class Features():
    """
    Creates and manages a collection of all features for a particular usage.
    """
    def __init__(self):
        """
        Creates a fresh Features object and prepares a list to hold the collection of Feature objects
        """
        self.features_list = [] # The features storage list

    def return_list_of_all_feature_objects(self):
        """
        Returns a list of all feature objects
        """
        return self.features_list

    def count_number_of_individual_features_by_type(self, feature_type):
        """
        Return the number of the specified features found
        """
        counter = 0
        for feature in self.features_list:
            if feature.feature_number == feature_type:
                counter += 1
        return counter

    def add_feature(self, x_location, y_location, feature):
        """ 
        Add a fresh feature object to the features list
        """
        self.features_list.append(Feature(x_location, y_location, feature))

    def return_feature_value_by_coords(self, x_location, y_location):
        """
        Returns a single feature value from the Feature object associated with the passed x, y coordinates
        Returns 1 if not found
        """
        feature_value = 1
        for feature_object in self.features_list:
            if (x_location == feature_object.x_location) and (y_location == feature_object.y_location):
                feature_value = feature_object.feature_number
        return feature_value
    
    def return_relative_feature_value_by_coords(self, x_location, y_location, x_islandstart, y_islandstart):
        """
        Returns a single feature value from the Feature object based on the relative x, y coordinates required 
        as compared to the island's top-left coordinate
        Returns 1 if not found
        """
        feature_value = 1
        for feature_object in self.features_list:
            relative_x, relative_y = feature_object.return_relative_island_location(x_islandstart, y_islandstart)
            if (x_location == relative_x) and (y_location == relative_y):
                feature_value = feature_object.feature_number
        return feature_value
    
    def does_feature_type_already_exist(self, feature_type):
        """
        Checks to see if a feature specified exists
        """
        for feature in self.features_list:
            if feature == feature_type:
                return True
        return False
    