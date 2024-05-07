class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize empty board
        self.current_player = 'X'  # X starts the game

    def print_board(self):
        for i in range(0, 9, 3):
            print('| ' + ' | '.join(self.board[i:i+3]) + ' |')

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        else:
            print("Invalid move. That position is already taken.")
            return False

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

    def check_draw(self):
        return ' ' not in self.board

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            try:
                position = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            if 0 <= position <= 8:
                if self.make_move(position):
                    if self.check_winner():
                        print(f"Player {self.current_player} wins!")
                        break
                    elif self.check_draw():
                        print("It's a draw!")
                        break
                    else:
                        self.switch_player()
            else:
                print("Invalid input. Please enter a number between 1 and 9.")

# Start the game
game = TicTacToe()
game.play()
