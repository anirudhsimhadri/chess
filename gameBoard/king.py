import pygame
from BoardConstants import BoardConstants
from chessBoardMatrix import ChessBoardMatrix

class King():
    def __init__(self, color:str):
        self.pieceType = "king"
        self.color = color
        self.MaterialValue = 99
        self.hasMoved = False

        if self.color == "white":
            self.image = pygame.image.load('white_king.png').convert_alpha()
        elif self.color == "black":
            self.image = pygame.image.load('black_king.png').convert_alpha()
        
        self.cs = BoardConstants()

        self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))
    
    def move(self, x, y):
        """Kings move funtion"""
    
    def castle(self, x, y):
        """Kings castle funtion"""
        
    def is_valid_move(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
        matrix: ChessBoardMatrix
    ) -> bool:
        row_diff = end_row - start_row
        col_diff = end_col - start_col
        
        if abs(row_diff) > 1 or abs(col_diff) > 1: return False

        cap = matrix.chessboard[end_row][end_col]
        if cap != None and cap.color == self.color: return False
        
        return True

    def all_valid_moves(
        self,
        start_row: int,
        start_col: int,
        matrix: ChessBoardMatrix
    ) -> list[tuple[int, int]]:
        moves = [
            (start_row + 1, start_col),
            (start_row - 1, start_col),
            (start_row, start_col + 1),
            (start_row, start_col - 1),
            (start_row + 1, start_col + 1),
            (start_row + 1, start_col - 1),
            (start_row - 1, start_col + 1),
            (start_row - 1, start_col - 1)
        ]

        return [
            m for m in moves if self.is_valid_move(
                start_row,
                start_col,
                *m,
                matrix
            )
        ]
