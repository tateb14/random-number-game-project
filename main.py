def main():
    # set variables
    # calls menu()
    # directs choice to different functions with corresponding variables
    # recalls choice after each function
    # loops last 2 steps until quit
    
    game_range_min = 1 #Default min range
    game_range_max = 1000 #Default max range
    loop_primer = 1 #Primes loop
    
    choice = menu() # Call menu and get the choice
    
    #loop
    while loop_primer == 1:
        if choice == 1: #Start New Game
            player_1, player_2 = get_player()
            game(game_range_min, game_range_max, player_1, player_2)
            choice = menu()
            
        elif choice == 2: #Choose Range
            game_range_min, game_range_max = num_gen()
            choice = menu()
        
        elif choice == 3: #Exit Program
            loop_primer = 0

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
    pass

def num_gen():
    pass

def guess_num():
    pass
