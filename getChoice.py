# getChoice.py

def get_choice():
    # get_choice accepts no args
    # which will prompt the user to input a number
    # this will validate the inputted number
    # return the correct output, starting a new game
    # choosing a range
    # or exitting the program.
    print("Welcome to the random number guessing game! Please select one of the options below!\n\n1: Start a new game\n2: Define a new range\n3: Exit") # Displays the legend
    choice = int(input(">: ")) # Prompts the user for the choice
    
    while choice < 1 or choice > 3: # Validates the choice and prompts the user to reinput the number if required
        choice = int(input("Please input a valid number between 1-3: "))
    
    return choice # Returns choice
