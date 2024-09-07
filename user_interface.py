
class UserInterface():
    """
        Class representing the user interface in the game
    """

    def __init__(self):
        """
            Sets up the game loop that provides output and receives input from the user
        """
        exitFlag = False
        print("Welcome to Carrier Directive")
        print("By Barrie Millar")
        print("A text-mode strategic game inspired by the 1988 game Carrier Command")
        print("\n\nDebug mode enabled by default:")
        print('Please enter your next command or "help" for more information\n')
        while (exitFlag == False):
            command = input()
            print("\n")
            if command.lower() == "help":
                print("Commands available\n\n")
                print("quit - Quits the game")
                print("\n")



