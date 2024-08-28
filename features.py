
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
    
    def does_feature_type_already_exist(self, feature_type):
        for feature in self.features_list:
            if feature == feature_type:
                return True
        return False
    