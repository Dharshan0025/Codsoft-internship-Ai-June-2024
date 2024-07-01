class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)
    
    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False
    
    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)
    
    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def get_empty_cells(self):
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    empty_cells.append((i, j))
        return empty_cells

    def ai_move(self):
        empty_cells = self.get_empty_cells()
        if not empty_cells:
            return None
        
        best_score = -float('inf')
        best_move = None
        
        for move in empty_cells:
            self.board[move[0]][move[1]] = 'O'
            score = self.minimax(False)
            self.board[move[0]][move[1]] = ' '
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def minimax(self, is_maximizing):
        if self.check_winner('O'):
            return 1
        elif self.check_winner('X'):
            return -1
        elif self.is_full():
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        score = self.minimax(False)
                        self.board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        score = self.minimax(True)
                        self.board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score
    
    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.print_board()
        
        while True:
            if self.current_player == 'X':
                while True:
                    try:
                        row, col = map(int, input("Enter your move (row col): ").split())
                        if self.make_move(row, col):
                            break
                        else:
                            print("Invalid move. Try again.")
                    except ValueError:
                        print("Invalid input format. Please enter two integers separated by space.")
            else:
                print("AI is making a move...")
                ai_move = self.ai_move()
                if ai_move:
                    self.board[ai_move[0]][ai_move[1]] = 'O'
                
            self.print_board()
            
            if self.check_winner(self.current_player):
                print(f"Congratulations! {self.current_player} wins!")
                break
            
            if self.is_full():
                print("It's a draw!")
                break
            
            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
