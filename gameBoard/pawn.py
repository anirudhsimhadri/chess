import pygame
from BoardConstants import BoardConstants
from chessBoardMatrix import ChessBoardMatrix as cbm

class Pawn():
    def __init__(self, color:str):
        self.pieceType = "pawn"
        self.color = color
        self.MaterialValue = 1
        self.hasMoved = False

        if self.color == "white":
            self.image = pygame.image.load('white_pawn.png').convert_alpha()
        elif self.color == "black":
            self.image = pygame.image.load('black_pawn.png').convert_alpha()
        
        self.cs = BoardConstants()

        self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))
    
    
    def is_valid_move(self, row, col, target_row, target_col, matrix: cbm):
        #Check if the pawn can move to the target location
        if self.color == "white":
            if target_row == row - 2 and target_col == col and not self.hasMoved and (matrix.chessboard[row - 1][col] == None):
                return True
            elif target_row == row - 1 and target_col == col and not matrix.chessboard[target_row][target_col]:
                return True
            elif target_row == row - 1 and abs(target_col - col) == 1 and matrix.chessboard[target_row][target_col] and matrix.chessboard[target_row][target_col].color != self.color:
                return True
        elif self.color == "black":
            if target_row == row + 2 and target_col == col and not self.hasMoved and (matrix.chessboard[row + 1][col] == None):
                return True
            elif target_row == row + 1 and target_col == col and not matrix.chessboard[target_row][target_col]:
                return True
            elif target_row == row + 1 and abs(target_col - col) == 1 and matrix.chessboard[target_row][target_col] and matrix.chessboard[target_row][target_col].color != self.color:
                return True
        return False
        