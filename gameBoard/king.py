import pygame
from BoardConstants import BoardConstants
from chessBoardMatrix import ChessBoardMatrix

class King():
    def __init__(self, color:str):
        self.pieceType = "king"
        self.color = color
        self.MaterialValue = 99
        self.hasMoved = False
        # Backup value for `self.hasMoved`, used to preserve state after `undoMove()`
        self.hasMovedBefore = False

        #if self.color == "white":
        #    self.image = pygame.image.load('white_king.png').convert_alpha()
        #elif self.color == "black":
        #    self.image = pygame.image.load('black_king.png').convert_alpha()
        
        self.cs = BoardConstants()

        #self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))
    
    def is_valid_move(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
        matrix: ChessBoardMatrix
    ) -> bool:
        if not self.hasMoved:
            # Castling logic (doesn't check if traveled squares are threatened)
            if end_col == 2:
                rook = matrix.chessboard[start_row][0]

                if rook is None: return False
                if rook.pieceType != "rook": return False
                if rook.hasMoved: return False

                if matrix.chessboard[start_row][1] is not None: return False
                if matrix.chessboard[start_row][2] is not None: return False
                if matrix.chessboard[start_row][3] is not None: return False
                
                return True
            else:
                assert end_col == 6
                rook = matrix.chessboard[start_row][7]

                if rook is None: return False
                if rook.pieceType != "rook": return False
                if rook.hasMoved: return False

                if matrix.chessboard[start_row][5] is not None: return False
                if matrix.chessboard[start_row][6] is not None: return False

                return True

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

        moves = [
            m for m in moves if (
                m[0] >= 0 and m[0] < 8 and m[1] >= 0 and m[1] < 8
            )
        ]

        return [
            m for m in moves if self.is_valid_move(
                start_row,
                start_col,
                *m,
                matrix
            )
        ]
