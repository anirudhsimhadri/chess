import pygame
from BoardConstants import BoardConstants

class Pawn():
    def __init__(self, color:str):
        self.type = "pawn"
        self.color = color
        self.MaterialValue = 1
        self.hasMoved = False

        if self.color == "white":
            self.image = pygame.image.load('chess/1x/w_pawn_1x.png')
        elif self.color == "black":
            self.image = pygame.image.load('chess/1x/b_pawn_1x.png')
        
        self.cs = BoardConstants()

        self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))
    
    def move(self, row, col, target_row, target_col):
        #Move the pawn to the target location
        self.row = target_row
        self.col = target_col
        self.hasMoved = True #set to True so the pawn cant move two squares forward
    
    def valid_move(self, row, col, target_row, target_col):
        #Check if the pawn can move to the target location
        if self.color == "white":
            if target_row == row - 1 and target_col == col and not self.hasMoved:
                return True
            elif target_row == row - 1 and target_col == col and not self.chessboard[target_row][target_col]:
                return True
            elif target_row == row - 1 and abs(target_col - col) == 1 and self.chessboard[target_row][target_col] and self.chessboard[target_row][target_col].color != self.color:
                return True
        elif self.color == "black":
            if target_row == row + 1 and target_col == col and not self.hasMoved:
                return True
            elif target_row == row + 1 and target_col == col and not self.chessboard[target_row][target_col]:
                return True
            elif target_row == row + 1 and abs(target_col - col) == 1 and self.chessboard[target_row][target_col] and self.chessboard[target_row][target_col].color!= self.color:
                return True
        return False
    def en_pessant(self, x, y):
        """"pawn en pessant capability"""
        