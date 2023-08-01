import pygame
from BoardConstants import BoardConstants
from chessBoardMatrix import ChessBoardMatrix as cbm

class Queen():
    def __init__(self, color:str):
        self.pieceType = "queen"
        self.color = color
        self.MaterialValue = 9

        if self.color == "white":
            self.image = pygame.image.load('white_queen.png').convert_alpha()
        elif self.color == "black":
            self.image = pygame.image.load('black_queen.png').convert_alpha()
        
        self.cs = BoardConstants()

        self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))

    """
    def is_valid_move(self, row, col, target_row, target_col, matrix: cbm):
        row_diff = target_row - row
        col_diff = target_col - col

        if abs(row_diff) != abs(col_diff): return False
        if target_row >= 8 or target_col >= 8: return False

        dir = (
            1 if row_diff > 0 else -1,
            1 if col_diff > 0 else -1
        )
        pos = row, col

        for i in range(1, abs(row_diff)):
            pos = (
                pos[0] + dir[0],
                pos[1] + dir[1]
            )

            if matrix.chessboard[pos[0]][pos[1]] != None:
                return False
        
        cap = matrix.chessboard[target_row][target_col]
        if cap != None and cap.color == self.color: return False

        return True"""