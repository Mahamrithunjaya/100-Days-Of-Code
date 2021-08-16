class Board:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "❌"

    def draw_board(self):
        print(f"{self.turn}'s Turn")
        print(f"""
                {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}
                ---|---|---
                {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}
                ---|---|---
                {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}
        """)

    def mark(self, loc):
        """This will plot the location in the board according to the user's input"""
        if len(loc) == 2:
            try:
                row = int(loc[0]) - 1
                column = int(loc[1]) - 1
                cell = self.board[row][column]

                if cell == " ":
                    self.board[row][column] = self.turn
                    return True
                else:
                    print("\n Cell is already taken!")
                    return False
            except:
                print(f"\n[☞] Something Went Wrong...!!, You entered ➔ {loc}\n Try Again!!!")
                return False
        else:
            print("\n[☞] Invalid Co-Ordinates!!, Try Again...")
            return False

    def check_player_x(self):
        """This checks the winning positions for the player with X symbol and if it matches returns True"""

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
        """This checks the winning positions of the player with symbol O and if it matches returns True """

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

    def check_draw(self):
        """This checks whether the game is draw or not. Draw game means all the cells are filled but none of them are
        in position to win."""
        draw = True
        for row in self.board:
            for cell in row:
                if cell == " ":
                    draw = False
        return draw

    def switch_turn(self):
        """This will switch the symbol for the player."""
        if self.turn == "❌":
            self.turn = "⭕"
        else:
            self.turn = "❌"

    def check_winner(self):
        """This will check the winner of the game."""
        if self.check_player_x():
            return True, "❌"
        elif self.check_player_o():
            return True, "⭕"
        elif self.check_draw():
            return True, "DRAW"
        else:
            return False, None
