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

def get_players():
    # get_players accepts no args
    # it will prompt the user to input the
    # names for player 1 and player 2
    # returns both player names
    
    p1 = input("Please enter the name of player 1: ")
    p2 = input("Please enter the name of player 2: ")
    
    return p1, p2

def num_gen(MIN_MUMBER, MAX_NUMBER):
    # num_gen accepts MIN_NUMBER and MAX_NUMBER
    # it will generate a number
    # between the specified range
    # returns the number
    import random
    
    game_number = random.randint(MIN_NUMBER, MAX_NUMBER) # randomly calls a new number
    return game_number # returns that number

def guess_num(game_range_min, game_range_max, player_1, player_2):
    # guess_num will accept 4 arguments (the min and max number and player names)
    # it will call num_gen to generate a number
    # makes player 1 and 2 take turns guessing a number (looped)
    # after guessing returns feedback and a hint
    # keep tracks of number of turns
    # when random number has been guessed, display winner and num of turns
    number = num_gen(game_range_min, game_range_max)
    guess = 0
    turns = 0
    player_turn = 1
    
    while guess != number:
        if player_turn = 1: #player 1 turn
            guess = input(player_1, ", guess a number between ", game_range_min, " and ", game_range_max, sep='')
            while guess < game_range_min or guess > game_range_max: # validation
                guess = int(input("Please input a valid number between", game_range_min, " and ", game_range_max, sep=''))
            if guess < number: # compares guess to number
                print("The number is higher")
            elif guess > number:
                print("The number is lower")
            elif guess == number:
                print(player_1, "has won, the number was" number)
            player_turn = 2 #sets it to player 2 turn
            
        elif player_turn = 2: #player 2 turn
            guess = input(player_2, ", guess a number between ", game_range_min, " and ", game_range_max, sep='')
            while guess < game_range_min or guess > game_range_max: # validation
                guess = int(input("Please input a valid number between", game_range_min, " and ", game_range_max, sep=''))
            if guess < number: # compares guess to number
                print("The number is higher")
            elif guess > number:
                print("The number is lower")
            elif guess == number:
                print(player_2, "has won, the number was" number)
            player_turn = 3 #sets it to 3 to change turn counter
        
        elif player_turn = 3
            turns += 1 # adds 1 to turn counter
            player_turn = 1 #sets it to player 1 turn
        
    
                
       
        
        
        
        
        
        
        
    
