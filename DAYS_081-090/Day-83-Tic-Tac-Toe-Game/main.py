from art import logo1, logo2
from board import Board


def main():
    board = Board()

    while True:
        board.draw_board()

        position = input(f"Enter the co-ordinates to plot {board.turn}: ")
        placed = board.mark(position)

        game_over, winner = board.check_winner()

        if placed:
            if not game_over:
                board.switch_turn()
            else:
                board.draw_board()
                print("\n Game Over")
                if winner != "DRAW":
                    print(f"{winner} won!!")
                else:
                    print("It's a DRAW!!")
                break


if __name__ == "__main__":
    print(logo1)
    print(logo2)
    print("\n Enter to start")
    input()
    main()
