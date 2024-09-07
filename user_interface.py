
class UserInterface():
    """
        Class representing the user interface in the game
    """

    def __init__(self):
        """
            Sets up the game loop that provides output and receives input from the user
        """
        exitFlag = False
        print("\nWelcome to Carrier Directive")
        print("By Barrie Millar")
        print("A text-mode strategic game inspired by the 1988 game Carrier Command")
        print("\nDebug mode enabled by default\n")
        while (exitFlag == False):
            print('Please enter a command or "h" for more information')
            command = input()
            if command.lower() == "h":
                print("\nCommands available\n")
                print("quit - Quits the game\n")
            elif command.lower() == "quit":
                break
            



