class Piece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"{self.name[0]}{self.color[0]}"

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        for i in range(8):
            self.board[1][i] = Piece('black', 'pawn')
            self.board[6][i] = Piece('white', 'pawn')
        
        pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        for i, piece in enumerate(pieces):
            self.board[0][i] = Piece('black', piece)
            self.board[7][i] = Piece('white', piece)

    def print_board(self):
        for row in self.board:
            print(' '.join([str(piece) if piece else '  ' for piece in row]))

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        if self.board[start_row][start_col] is None:
            print("No piece at starting position.")
            return False
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = None
        return True

def main():
    board = Board()
    board.print_board()
    game_over = False
    while not game_over:
        start_pos = tuple(map(int, input("Enter start position (row col): ").split()))
        end_pos = tuple(map(int, input("Enter end position (row col): ").split()))
        moved = board.move_piece(start_pos, end_pos)
        if moved:
            board.print_board()
        else:
            print("Invalid move, try again.")
        # Add conditions to check for checkmate or stalemate to end the game

if __name__ == "__main__":
    main()

