class Board:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "❌"

    def draw_board(self):
        print(f"{self.turn}'s Turn")
        print(f"""
{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}
----|----|----
{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}
----|----|----
{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}
""")

    def mark(self, loc):
        if len(loc) == 2:
            row = int(loc[0] - 1)
            column = int(loc[1] - 1)
            cell = self.board[row][column]

            if cell == " ":
                self.board[row][column] = self.turn
            else:
                print("\n Cell is already taken!")
                return False
        else:
            print("\n Invalid Co-Ordinates!!, Try Again...")
            return False

    def check_player_x(self):

        # Checking Rows
        if self.board[0][0] == "❌" and self.board[0][1] == "❌" and self.board[0][2] == "❌":
            return True
        elif self.board[1][0] == "❌" and self.board[1][1] == "❌" and self.board[1][2] == "❌":
            return True
        elif self.board[2][0] == "❌" and self.board[2][1] == "❌" and self.board[2][2] == "❌":
            return True

        # Checking Columns
        elif self.board[0][0] == "❌" and self.board[1][0] == "❌" and self.board[2][0] == "❌":
            return True
        elif self.board[0][1] == "❌" and self.board[1][1] == "❌" and self.board[2][1] == "❌":
            return True
        elif self.board[0][2] == "❌" and self.board[1][2] == "❌" and self.board[2][2] == "❌":
            return True

        # Checking Diagonals
        elif self.board[0][0] == "❌" and self.board[1][1] == "❌" and self.board[2][2] == "❌":
            return True
        elif self.board[0][2] == "❌" and self.board[1][1] == "❌" and self.board[2][0] == "❌":
            return True
        else:
            return False

    def check_player_o(self):

        # Checking Rows
        if self.board[0][0] == "⭕" and self.board[0][1] == "⭕" and self.board[0][2] == "⭕":
            return True
        elif self.board[1][0] == "⭕" and self.board[1][1] == "⭕" and self.board[1][2] == "⭕":
            return True
        elif self.board[2][0] == "⭕" and self.board[2][1] == "⭕" and self.board[2][2] == "⭕":
            return True

        # Checking Columns
        elif self.board[0][0] == "⭕" and self.board[1][0] == "⭕" and self.board[2][0] == "⭕":
            return True
        elif self.board[0][1] == "⭕" and self.board[1][1] == "⭕" and self.board[2][1] == "⭕":
            return True
        elif self.board[0][2] == "⭕" and self.board[1][2] == "⭕" and self.board[2][2] == "⭕":
            return True

        # Checking Diagonals
        elif self.board[0][0] == "⭕" and self.board[1][1] == "⭕" and self.board[2][2] == "⭕":
            return True
        elif self.board[0][2] == "⭕" and self.board[1][1] == "⭕" and self.board[2][0] == "⭕":
            return True
        else:
            return False
        