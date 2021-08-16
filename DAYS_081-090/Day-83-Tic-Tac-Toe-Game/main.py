from art import logo1, logo2
from board import Board
import time
import os


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    board = Board()

    while True:
        board.draw_board()

        position = input(f"Enter the co-ordinates to plot {board.turn}: ")
        placed = board.mark(position)

        game_over, winner = board.check_winner()

        if placed:
            if not game_over:
                clear()
                board.switch_turn()
            else:
                clear()
                board.draw_board()
                print("\n   GAME OVER \n")
                if winner != "DRAW":
                    print(f" Player '{winner}' WON THE GAME!!")
                else:
                    print(" IT'S A DRAW!!")
                break
        else:
            time.sleep(1)
            clear()


if __name__ == "__main__":
    print(logo1)
    print(logo2)
    print("\n[☆] PRESS ENTER TO VIEW THE RULES TO PLAY..............")
    input()
    clear()

    main()
