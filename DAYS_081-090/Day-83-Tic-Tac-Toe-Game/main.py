from art import logo1, logo2
from board import Board
import time
import os

GAME_POSITIONS = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def rules():
    print("\n Rule 1 : Always User1 Makes The First Move")
    print("\n Rule 2 : This game is based on matrix positions."
          "\n           So you need to give positions as 'ij'."
          "\n           Where 'i' = 'row' and 'j' = 'column'")

    print("\n\n")

    print("         ----------      -----------------------")
    print("         | BOARD  |     | POSITIONS TO BE ENTER | ")
    print("         ----------      -----------------------\n")
    print("         X | O | X          11 | 12 | 13")
    print("         - - - - -        - - - - - - - - - -")
    print("         X | O | X          21 | 22 | 23 ")
    print("         - - - - -        - - - - - - - - - -")
    print("         X | O | X          31 | 32 | 33 \n\n")

    time.sleep(4)
    print("\n    About to Start....")
    time.sleep(3)
    print("\n    Best of LUCK.......")
    time.sleep(0.8)
    clear()

    for i in range(2):
        print("   ☐\n     ☐\n   ☐   \n     ☐\n\n GAME LOADING . ")
        time.sleep(0.7)
        clear()

        print("\n   ☐ ☐\n   ☐ ☐\n\n GAME LOADING . .")
        time.sleep(0.7)
        clear()

        print("     ☐\n   ☐  \n     ☐\n   ☐  \n\n GAME LOADING . . .")
        time.sleep(0.7)
        clear()

        print("\n   ☐ ☐\n   ☐ ☐\n\n GAME LOADING .")
        time.sleep(0.7)
        clear()

        print("\n    ☐ ☐\n   ☐ ☐\n\n GAME LOADING . .")
        time.sleep(0.7)
        clear()

        print("\n   ☐ ☐\n   ☐ ☐\n\n GAME LOADING . . .")
        time.sleep(0.7)
        clear()

        print("\n   ☐ ☐\n    ☐ ☐\n\n GAME LOADING . ")
        time.sleep(0.7)
        clear()

        print("\n   ☐ ☐\n   ☐ ☐\n\n GAME LOADING . .")
        time.sleep(0.7)
        clear()
    print("\n\n\n    FINISHED LOADING...")
    time.sleep(1)
    clear()


def main(turn):
    board = Board(turn)

    while True:
        board.draw_board()

        position = input(f"\n Enter the co-ordinates to plot {board.turn}: ")
        placed = board.player_move(position)

        game_over, winner = board.check_winner()

        if placed:
            if not game_over:
                clear()
                board.switch_turn()
            else:
                clear()
                board.draw_board()
                print("\n   GAME OVER \n\n")
                if winner != "DRAW":
                    print(f" Player '{winner}' WON THE GAME!!")
                    time.sleep(5)
                else:
                    print("\n IT'S A DRAW!!")
                break
        else:
            time.sleep(1)
            clear()


def auto_player(turn):
    board = Board(turn)

    while True:
        board.draw_board()

        position = input(f" Enter the co-ordinates to plot {board.turn}: ")
        placed = board.player_move(position)

        game_over, winner = board.check_winner()

        if placed:
            if not game_over:
                clear()
                GAME_POSITIONS.remove(position)
                board.switch_turn()
                comp_check, comp_pos = board.computer_player(GAME_POSITIONS)
                auto_over = comp_check[0]
                won = comp_check[1]
                # print(auto_over, ",", won)
                # print(comp_pos)
                GAME_POSITIONS.remove(comp_pos)
                if auto_over:
                    board.draw_board()
                    print("\n   GAME OVER \n\n")
                    if won != "DRAW":
                        print(f"\n SORRY!!! THIS TIME COMPUTER WON THE GAME!!")
                        time.sleep(5)
                    else:
                        print("\n IT'S A DRAW!!")
                    break
                board.switch_turn()

            else:
                clear()
                board.draw_board()
                print("\n   GAME OVER \n\n")
                if winner != "DRAW":
                    print(f"\n Player '{winner}' WON THE GAME!!")
                    time.sleep(5)
                else:
                    print("\n IT'S A DRAW!!")
                break
        else:
            time.sleep(1)
            clear()


def player_selection():
    while True:
        player_choice = input("\n\n Please select any one option from below: \n (a) 'Single Player(vs Computer)' \n ("
                              "b) 'Multiple-Player \n ")
        if player_choice == "a":
            return "a"
        elif player_choice == "b":
            return "b"
        else:
            print("\n Invalid Selection!! Select any one 'a' or 'b'.")
            time.sleep(1)
            clear()


def symbol_selection():
    while True:
        symbol_choice = input("\n\n Please select any option of the symbol: \n (a) 'X' \n (b) 'O' \n ")
        if symbol_choice == "a":
            symbol_of_player = "X"
            print("\n You have selected 'X' symbol for the game.\n Your opponent will have 'O' symbol.")
            return symbol_of_player
        elif symbol_choice == "b":
            symbol_of_player = "O"
            print("\n You have selected 'O' symbol for the game.\n Your opponent will have 'X' symbol.")
            return symbol_of_player
        else:
            print("\n Invalid Selection!! Select any one 'a' or 'b'")
            time.sleep(1)
            clear()


if __name__ == "__main__":
    print(logo1)
    print(logo2)

    print("\n[*] PRESS ENTER TO VIEW THE RULES TO PLAY..............")
    input()
    clear()
    rules()

    print("\n\n[*] PRESS ENTER TO CONTINUE..............")
    input()
    clear()

    symbol = symbol_selection()
    time.sleep(2)
    clear()

    player = player_selection()
    clear()
    if player == "a":
        auto_player(symbol)
    else:
        main(symbol)
        time.sleep(1)

    while True:
        answer = input("Do you want to play again? (Y/N)")
        if answer.lower() == "y" or answer.lower() == "yes":
            clear()
            symbol = symbol_selection()
            time.sleep(2)
            clear()

            player = player_selection()
            clear()
            if player == "a":
                auto_player(symbol)
            else:
                main(symbol)
                time.sleep(1)
        else:
            print("\n\n  GOODBYE ")
            time.sleep(1.5)
            break
