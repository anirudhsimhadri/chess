import pygame
from BoardConstants import BoardConstants
from chessBoardMatrix import ChessBoardMatrix as cbm

class Knight():
    def __init__(self, color:str):
        self.pieceType = "knight"
        self.color = color
        self.MaterialValue = 3

        if self.color == "white":
            self.image = pygame.image.load('white_knight.png').convert_alpha()
        elif self.color == "black":
            self.image = pygame.image.load('black_knight.png').convert_alpha()
        
        self.cs = BoardConstants()

        self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))

    def is_valid_move(self, row, col, target_row, target_col, matrix: cbm):
        """checks if the desired move is valid"""

        #checks if the target location is valid
        print(target_col, target_row, "KNIGHT")
        location = (matrix.chessboard[target_row][target_col] == None or matrix.chessboard[target_row][target_col].color != matrix.chessboard[row][col].color)

        #checking if the designated location is valid according to knights movement rules
        if ((target_col == col - 1 and target_row == row + 2 and (location)) or 
            (target_col == col - 1 and target_row == row - 2 and (location)) or 
            (target_col == col - 2 and target_row == row + 1 and (location)) or 
            (target_col == col - 2 and target_row == row - 1 and (location)) or 
            (target_col == col + 1 and target_row == row + 2 and (location)) or 
            (target_col == col + 1 and target_row == row - 2 and (location)) or 
            (target_col == col + 2 and target_row == row + 1 and (location)) or 
            (target_col == col + 2 and target_row == row - 1 and (location))):
            return True
        else:
            return False
        