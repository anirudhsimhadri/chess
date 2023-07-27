import pygame
from chessBoardMatrix import ChessBoardMatrix
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

    def valid_move(
        self,
        start_row,
        start_col,
        end_row,
        end_col,
        mat: ChessBoardMatrix
    ) -> bool:
        row_diff = end_row - start_row
        col_diff = abs(end_col - start_col)

        if abs(row_diff) != abs(col_diff): return False
        if end_row >= 8 or end_col >= 8: return False

        dir = (
            1 if row_diff > 0 else -1,
            1 if col_diff > 0 else -1
        )
        pos = start_row, start_col

        for i in range(1, row_diff):
            pos = (
                pos[0] + dir[0],
                pos[1] + dir[1]
            )

            if mat.chessboard[pos[0]][pos[1]] != None:
                return False

        return True
