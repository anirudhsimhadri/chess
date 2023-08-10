import pygame
from BoardConstants import BoardConstants
from chessBoardMatrix import ChessBoardMatrix as cbm

"""
Two Player Lan Chess
By: Sam Aven, Ani Simhadri, Andrew Voss
This project was created during an intership with PRI Global
Purpose of this file: Handles all knight functionality
"""
class Knight():
    def __init__(self, color:str):
        self.pieceType = "knight"
        self.color = color
        self.MaterialValue = 3

        #if self.color == "white":
        #    self.image = pygame.image.load('white_knight.png').convert_alpha()
        #elif self.color == "black":
        #    self.image = pygame.image.load('black_knight.png').convert_alpha()
        
        self.cs = BoardConstants()

        #self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))

    def is_valid_move(self, row, col, target_row, target_col, matrix: cbm):
        """checks if the desired move is valid"""

        #checks if the target location is valid
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
    
    def all_valid_moves(
        self,
        start_row: int,
        start_col: int,
        matrix: cbm
    ) -> list[tuple[int, int]]:
        # theres definitely a better way to generate this
        moves = [
            (start_row + 2, start_col - 1),
            (start_row - 2, start_col - 1),
            (start_row + 1, start_col - 2),
            (start_row - 1, start_col - 2),
            (start_row + 2, start_col + 1),
            (start_row - 2, start_col + 1),
            (start_row + 1, start_col + 2),
            (start_row - 1, start_col + 2)
        ]

        moves = [
            (row, col) for (row, col) in moves if (
                row in range(8) and col in range(8)
                and self.is_valid_move(start_row, start_col, row, col, matrix)
            )
        ]

        return moves
        