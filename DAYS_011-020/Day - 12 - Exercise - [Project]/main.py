import random
import os
import time
import art
import loading

# Global Variables/Constants
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def check_answer(guess, answer, attempts):
    """ Checks answer(random number) against guess(user guessed number). Returns the number of turns(attempts)
    remaining. """

    if guess > answer:
        print(" Too high. ")
        return attempts - 1
    elif guess < answer:
        print(" Too Low. ")
        return attempts - 1
    else:
        print(f"\n You got it!  The answer was {answer}. ")


# Function to set difficulty by the user
def set_difficulty():
    level_choose = input("\n Choose a difficulty level. Type 'easy' or 'hard' : ").lower()
    if level_choose == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif level_choose == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        print(" INVALID INPUT !.... TRY AGAIN.....")
        exit()


# Main GAME function
def play_game():

    print("\n I'm thinking of a number between 1 and 100. ")
    # Choosing a random number between 1 and 100.
    random_number = random.randint(1, 100)
    turns = set_difficulty()

    user_guess = 0
    while user_guess != random_number:
        print(f"\n You have {turns} attempts remaining to guess the number. ")

        # Asking the user to guess a number
        user_guess = int(input("\n Make a Guess : "))

        turns = check_answer(guess=user_guess, answer=random_number, attempts=turns)
        # Track the number of turns and reduce it by 1 if the user guessed wrong number
        if turns == 0:
            print("\n You've run out of guesses, You Lose. ")
            exit()
        elif user_guess != random_number:
            print(" Guess Again. ")


def art_logos():

    print(art.welcome_logo)
    time.sleep(3)
    input('''
    ______                    _____      _              _____       _____             _   _                              
    | ___ \                  |  ___|    | |            |_   _|     /  __ \           | | (_)                             
    | |_/ / __ ___  ___ ___  | |__ _ __ | |_ ___ _ __    | | ___   | /  \/ ___  _ __ | |_ _ _ __  _   _  ___             
    |  __/ '__/ _ \/ __/ __| |  __| '_ \| __/ _ \ '__|   | |/ _ \  | |    / _ \| '_ \| __| | '_ \| | | |/ _ \            
    | |  | | |  __/\__ \__ \ | |__| | | | ||  __/ |      | | (_) | | \__/\ (_) | | | | |_| | | | | |_| |  __/  _ _ _ _ _ 
    \_|  |_|  \___||___/___/ \____/_| |_|\__\___|_|      \_/\___/   \____/\___/|_| |_|\__|_|_| |_|\__,_|\___| (_|_|_|_|_)
    ''')
    os.system('cls')

    for i in range(1):
        print(loading.load_logo[0])
        time.sleep(0.8)
        os.system('cls')

        print(loading.load_logo[1])
        time.sleep(0.8)
        os.system('cls')

        print(loading.load_logo[2])
        time.sleep(0.8)
        os.system('cls')

        print(loading.load_logo[3])
        time.sleep(0.8)
        os.system('cls')

        print(loading.load_logo[4])
        time.sleep(0.8)
        os.system('cls')

        print(loading.load_logo[5])
        time.sleep(0.8)
        os.system('cls')

    print(art.finish_logo)
    time.sleep(1.5)
    input('''
    ______                    _____      _              _____       _____             _   _                              
    | ___ \                  |  ___|    | |            |_   _|     /  __ \           | | (_)                             
    | |_/ / __ ___  ___ ___  | |__ _ __ | |_ ___ _ __    | | ___   | /  \/ ___  _ __ | |_ _ _ __  _   _  ___             
    |  __/ '__/ _ \/ __/ __| |  __| '_ \| __/ _ \ '__|   | |/ _ \  | |    / _ \| '_ \| __| | '_ \| | | |/ _ \            
    | |  | | |  __/\__ \__ \ | |__| | | | ||  __/ |      | | (_) | | \__/\ (_) | | | | |_| | | | | |_| |  __/  _ _ _ _ _ 
    \_|  |_|  \___||___/___/ \____/_| |_|\__\___|_|      \_/\___/   \____/\___/|_| |_|\__|_|_| |_|\__,_|\___| (_|_|_|_|_)                                                                                                                
    ''')
    os.system('cls')


art_logos()
os.system('cls')
play_game()
