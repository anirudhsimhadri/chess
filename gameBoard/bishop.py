import pygame
from BoardConstants import BoardConstants

class Bishop():
    def __init__(self, color:str):
        self.pieceType = "bishop"
        self.color = color
        self.MaterialValue = 3

        if self.color == "white":
            self.image = pygame.image.load('white_bishop.png').convert_alpha()
        elif self.color == "black":
            self.image = pygame.image.load('black_bishop.png').convert_alpha()
        
        self.cs = BoardConstants()

        self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))

    def valid_move(self, start_row, start_col, end_row, end_col) -> bool:
        row_diff = end_row - start_row
        col_diff = abs(end_col - start_col)

        return abs(row_diff) == abs(col_diff)
