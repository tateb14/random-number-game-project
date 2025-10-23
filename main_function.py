# main_function.py
#1 - main_function() <----
#2 - get_choice()
#3 - get_player()
#4 - num_gen()
#5 - game()

main_function() # Auto Call Main

def main_function():
    # set variables
    # calls get_choice()
    # directs choice to different functions with corresponding variables
    # recalls choice after each function
    # loops last 2 steps until quit
    
    game_range_min = 1 #Default min range
    game_range_max = 1000 #Default max range
    loop_primer = 1 #Primes loop
    
    choice = get_choice() # Call menu and get the choice
    
    #loop
    while loop_primer == 1:
        if choice == 1: #Start New Game
            player_1, player_2 = get_player()
            game(game_range_min, game_range_max, player_1, player_2)
            choice = get_choice()
            
        elif choice == 2: #Choose Range
            game_range_min, game_range_max = num_gen()
            choice = get_choice()
        
        elif choice == 3: #Exit Program
            loop_primer = 0
    
    
