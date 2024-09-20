
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
