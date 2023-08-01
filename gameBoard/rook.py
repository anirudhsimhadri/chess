import pygame
from BoardConstants import BoardConstants
from chessBoardMatrix import ChessBoardMatrix

class Rook():
    def __init__(self, color:str):
        self.pieceType = "rook"
        self.color = color
        self.MaterialValue = 5

        if self.color == "white":
            self.image = pygame.image.load('white_rook.png').convert_alpha()
        elif self.color == "black":
            self.image = pygame.image.load('black_rook.png').convert_alpha()
        
        self.cs = BoardConstants()

        self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))
    
    def is_valid_move(self, row, col, target_row, target_col, board):
        """
        Checks if the move is valid (it's a straight line and no piece is blocking the path).
        This doesn't check if the king would be in check after this move - that logic belongs elsewhere.
        """
        if target_row == row and (target_col in range(8)) and (board.chessboard[target_row][target_col] == None or board.chessboard[target_row][target_col].color != board.chessboard[row][col].color):
            return True
        elif target_col == col and (target_row in range(8)) and (board.chessboard[target_row][target_col] == None or board.chessboard[target_row][target_col].color != board.chessboard[row][col].color):
            return True
        else:
            return False
