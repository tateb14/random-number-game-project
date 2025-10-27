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
