import os
import random

# Intro to game
you = input("Type your NickName : \n--->")
print(" ")
print("Hello " + you + " ! Welcome to Rock, Paper, Scissors Game.")
print("This game works just like normal rock paper scissors. Just type the number corresponding to the item you want.")
print("Have Fun! \n")

# Main Game Function & Code
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_signs = [rock, paper, scissors]


def game_play(my_points=0, comp_points=0):

    user_choice = int(input("\n\nWhat do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"
                            "Type 404 to EXIT from game.\n"))

    if user_choice == 404:
        os.system('cls')
        print("\n\n")
        print(you + "'s Points: " + str(my_points))
        print("Computer's Points: " + str(comp_points))
        print("\n\nGAME FINISHED. To Play Once More Run the Code Again...")
        exit()

    if user_choice >= 3 or user_choice < 0:
        print("\nWe didn't Understand that!!  Please try a number from 0 to 2 . ")
        input("Press Enter To Continue...")
        game_play(my_points, comp_points)

    else:
        print("You Chose: ")
        print(game_signs[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer Chose: ")
        print(game_signs[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You Win ... You get 1 point!")
            my_points += 1
            print(you + "'s Points: " + str(my_points))
            print("Computer's Points: " + str(comp_points))
            game_play(my_points, comp_points)

        elif computer_choice == 0 and user_choice == 2:
            print("Computer Wins... Computer gets 1 point!")
            comp_points += 1
            print(you + "'s Points: " + str(my_points))
            print("Computer's Points: " + str(comp_points))
            game_play(my_points, comp_points)

        elif computer_choice > user_choice:
            print("Computer Wins... Computer gets 1 point!")
            comp_points += 1
            print(you + "'s Points: " + str(my_points))
            print("Computer's Points: " + str(comp_points))
            game_play(my_points, comp_points)

        elif user_choice > computer_choice:
            print("You Win ... You get 1 point!")
            my_points += 1
            print(you + "'s Points: " + str(my_points))
            print("Computer's Points: " + str(comp_points))
            game_play(my_points, comp_points)

        elif user_choice == computer_choice:
            print("It's a Draw Game... You both get 1/2 a point. ")
            my_points += 0.5
            comp_points += 0.5
            print(you + "'s Points: " + str(my_points))
            print("Computer's Points: " + str(comp_points))
            game_play(my_points, comp_points)


input("\nPress Enter To Continue........")
os.system('cls')
game_play()
