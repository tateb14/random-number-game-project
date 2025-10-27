def main():
    pass

def menu():
    pass

def start_game():
    pass

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

def choose_range():
    pass

def exit_game():
    pass

def get_players():
    # get_players accepts no args
    # it will prompt the user to input the
    # names for player 1 and player 2
    # returns both player names
    
    p1 = input("Please enter the name of player 1: ")
    p2 = input("Please enter the name of player 2: ")
    
    return p1, p2

def num_gen():
    # num_gen accepts no args
    # it will generate a number
    # between the specified range
    # returns the number
    import random
    MIN_NUMBER = 0 #defines the min and max numbers
    MAX_NUMBER = 100
    
    game_number = random.randint(MIN_NUMBER, MAX_NUMBER) # randomly calls a new number
    return game_number # returns that number

def guess_num():
    pass
