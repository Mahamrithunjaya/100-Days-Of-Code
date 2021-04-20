import random
import os
import time
import art
import loading_logos
from game_data import data


def display_format_data(account):
    """Takes the account data form game_data file and returns the printable format."""
    # Extract data from the dictionary
    name = account['name']
    description = account['description']
    country = account['country']
    # Debugging
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}. "


def check_followers(guess, followers_of_a, followers_of_b):
    """Take the user guess and follower counts and returns if they got it right."""
    if followers_of_a > followers_of_b:
        # Return True if guess is A and A has more followers than B either returns False
        return guess == "a"
    elif followers_of_b > followers_of_a:
        # Return True if guess is B and B has more followers than A either returns False
        return guess == "b"
    else:
        # Returns 'draw' if the comparison has same number of followers
        if guess == "a" or guess == "b":
            return 'draw'


def logo_display():
    print(art.welcome_logo)
    print(art.logo)
    time.sleep(3)
    os.system('cls')

    for i in range(1):
        print(loading_logos.load_logo[0])
        time.sleep(2.8)
        os.system('cls')

        print(loading_logos.load_logo[1])
        time.sleep(0.8)
        os.system('cls')

        print(loading_logos.load_logo[2])
        time.sleep(0.8)
        os.system('cls')

        print(loading_logos.load_logo[3])
        time.sleep(0.8)
        os.system('cls')

        print(loading_logos.load_logo[4])
        time.sleep(1.5)
        os.system('cls')

        print(loading_logos.load_logo[5])
        time.sleep(0.8)
        os.system('cls')

        print(loading_logos.load_logo[6])
        time.sleep(0.8)
        os.system('cls')

        print(loading_logos.load_logo[7])
        time.sleep(0.8)
        os.system('cls')

    print(loading_logos.enter_logo)
    time.sleep(1)
    input("↵")
    os.system('cls')


def play_game():
    # Display Art
    os.system('cls')
    print(art.logo2)
    print("  IT'S A GAME ON THE BASIS OF INSTAGRAM FOLLOWERS COUNT..")
    score = 0
    # Generate a random account from the game data.
    account_b = random.choice(data)
    continue_game = True

    # Make the game repeatable.
    while continue_game:

        # Making account at position B become the next account at position A.
        account_a = account_b
        account_b = random.choice(data)

        # Making another random choice if there is same data in both account_a and account_b
        while account_a == account_b:
            account_b = random.choice(data)

        # Printing the Comparing data to the screen
        print(f"  Compare A : {display_format_data(account=account_a)}")
        print(art.vs)
        print(f"  Against B : {display_format_data(account=account_b)}")

        # Ask user for a guess.
        follower_check = input("\n  Who has more followers? Type 'A' or 'B' : ").lower()

        # Check if user is correct.
        # Get follower count of each account.
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']

        is_correct = check_followers(guess=follower_check, followers_of_a=a_follower_count,
                                     followers_of_b=b_follower_count)

        # Clear the screen between rounds.
        os.system('cls')
        print(art.logo2)

        # Give user feedback on their guess.
        # Score keeping.
        if is_correct == 'draw':
            score += 0.5
            print(f"\n  It's Draw because both have same count of followers. Current Score : {score}")
        elif is_correct:
            score += 1
            print(f"\n  You're right! Current score : {score}")
        else:
            continue_game = False
            print(f"\n  Sorry, that's wrong.\n  Your Final score : {score}")


logo_display()
os.system('cls')
play_game()
