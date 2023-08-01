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

        if abs(row_diff) != abs(col_diff): return False
        if end_row >= 8 or end_col >= 8: return False

        dir = (
            1 if row_diff > 0 else -1,
            1 if col_diff > 0 else -1
        )
        pos = start_row, start_col

        for i in range(1, abs(row_diff)):
            pos = (
                pos[0] + dir[0],
                pos[1] + dir[1]
            )

            if matrix.chessboard[pos[0]][pos[1]] != None:
                return False
        
        cap = matrix.chessboard[end_row][end_col]
        if cap != None and cap.color == self.color: return False

        return True
    
    def all_valid_moves(
        self,
        start_row: int,
        start_col: int,
        matrix: ChessBoardMatrix
    ) -> list[tuple[int, int]]:
        dirs: list[tuple[int, int]] = [
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]

        moves: list[tuple[int, int]] = []

        for dir in dirs:
            pos = (start_row, start_col)
            while True:
                pos = (
                    pos[0] + dir[0],
                    pos[1] + dir[1]
                )
                if (pos[0] < 0 or pos[0] >= 8
                or pos[1] < 0 or pos[1] >= 8):
                    break

                target = matrix.chessboard[pos[0]][pos[1]]
                if target == None:
                    moves.append(pos)
                elif target.color != self.color:
                    moves.append(pos)
                    break
                else:
                    break
        
        return moves
