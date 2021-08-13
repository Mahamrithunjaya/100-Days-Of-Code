import random
import os
import time
import art
import cards_symbol


def deal_card():
    """ Returns a random card from the Deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """ Take a list of cards and return the score calculated from the cards"""

    # Checking up if the user or computer have a blackjack
    # black_jack represents 0
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_scores, computer_scores):
    if user_scores > 21 and computer_scores > 21:
        return "\n You went over. You lose 😤"

    if computer_scores == user_scores:
        return "\n It's a DRAW. 🙃 "
    elif computer_scores == 0:
        return "\n Lose, opponent(Dealer) has Blackjack 😱 "
    elif user_scores == 0:
        return "\n You Win with a Blackjack. 😎"
    elif user_scores > 21:
        return "\n You went over. You lose. 😭"
    elif computer_scores > 21:
        return "\n Opponent went over. You win. 😁 "
    elif user_scores > computer_scores:
        return "\n You Win 😃"
    else:
        return "\n You Lose 😤"


def play_game():
    print(art.logo)

    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\n Your cards: {user_cards}, current score : {user_score}")
        print(f"\n Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("\n Type 'y' to get another card , type 'p' to pass : ")
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\n Your Final Hand : {user_cards} and Final Score is : {user_score}")
    print(f"\n Computer's Final Hand : {computer_cards} and Final Score is : {computer_score}")
    print(compare(user_scores=user_score, computer_scores=computer_score))


# Welcome
print(art.welcome_logo)
time.sleep(3)
input(" Press Enter to continue ...........")
os.system('cls')

for i in range(2):
    print(cards_symbol.cards_logo[0])
    time.sleep(1)
    os.system('cls')

    print(cards_symbol.cards_logo[1])
    time.sleep(1)
    os.system('cls')

    print(cards_symbol.cards_logo[2])
    time.sleep(1)
    os.system('cls')

    print(cards_symbol.cards_logo[3])
    time.sleep(1)
    os.system('cls')

print(art.finish_load)
time.sleep(1)
input('''

     __   __   ___  __   __      ___      ___  ___  __     ___  __      __   __       ___              ___          
    |__) |__) |__  /__` /__`    |__  |\ |  |  |__  |__)     |  /  \    /  ` /  \ |\ |  |  | |\ | |  | |__           
    |    |  \ |___ .__/ .__/    |___ | \|  |  |___ |  \     |  \__/    \__, \__/ | \|  |  | | \| \__/ |___    ..........
                                                                                                                                                                                                                             
''')
os.system('cls')

while input("\n Do you want to play a game of BlackJack? Type 'y' or 'n' : ") == "y":
    os.system('cls')
    play_game()

