import random
import time
import os
import hangman_art
import hangman_win
import hangman_words


for i in range(1):
    print(hangman_art.stages[6])
    print("\n Loading . . . .")
    time.sleep(1)
    os.system('cls')

    print(hangman_art.stages[5])
    print("\n Loading . . . .")
    time.sleep(1)
    os.system('cls')

    print(hangman_art.stages[4])
    print("\n Loading . . . .")
    time.sleep(1)
    os.system('cls')

    print(hangman_art.stages[3])
    print("\n Loading . . . .")
    time.sleep(1)
    os.system('cls')

    print(hangman_art.stages[2])
    print("\n Loading . . . .")
    time.sleep(1)
    os.system('cls')

    print(hangman_art.stages[1])
    print("\n Loading . . . .")
    time.sleep(1)
    os.system('cls')

    print(hangman_art.stages[0])
    print("\n Loading . . . .")
    time.sleep(1)
    os.system('cls')
print("FINISHED LOADING . . . . \n")
time.sleep(1)
os.system('cls')

# Printing HangMan Logo
print(hangman_art.logo)
print("\n\n FINAL CHECKING . . . . .")
time.sleep(3)
input("Press Enter to continue ...... ↵")

word_list = hangman_words.word_list
random_chosen_word = random.choice(word_list)
word_length = len(random_chosen_word)
lives = 6
win = False

# Testing Code
print("The Chosen Word is --->  ", random_chosen_word)

# Create Blanks
display = []
for each_letter in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:

    guess = input("Guess a Letter : ").lower()
    os.system('cls')

    # Check if user has entered a letter that has already guessed
    if guess in display:
        print(f"You have already guessed '{guess}'")

    # Check guessed letter
    for position in range(word_length):
        letter = random_chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user is wrong.
    if guess not in random_chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a Life. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose..!!!!!!")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        win = True
        for j in range(2):
            print(hangman_win.winning_art[0])
            time.sleep(1)
            os.system('cls')

            print(hangman_win.winning_art[1])
            time.sleep(1)
            os.system('cls')

            print(hangman_win.winning_art[2])
            time.sleep(1)
            os.system('cls')

    print(hangman_art.stages[lives])

if win is True:
    os.system('cls')
    print(hangman_win.winning_msg)
