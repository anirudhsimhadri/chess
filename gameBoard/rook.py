import pygame
from BoardConstants import BoardConstants
from chessBoardMatrix import ChessBoardMatrix

class Rook():
    def __init__(self, color:str):
        self.pieceType = "rook"
        self.color = color
        self.MaterialValue = 5

        if self.color == "white":
            self.image = pygame.image.load('white_rook.png').convert_alpha()
        elif self.color == "black":
            self.image = pygame.image.load('black_rook.png').convert_alpha()
        
        self.cs = BoardConstants()

        self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))
    
    def is_valid_move(self, row, col, target_row, target_col, board):
        """
        Checks if the move is valid (it's a straight line and no piece is blocking the path).
        This doesn't check if the king would be in check after this move - that logic belongs elsewhere.
        """
        row_diff = target_row - row
        col_diff = target_col - col


        if target_row == row and (target_col in range(8)) and (board.chessboard[target_row][target_col] == None or board.chessboard[target_row][target_col].color != board.chessboard[row][col].color):
            dir = (
            1 if row_diff > 0 else -1,
            1 if col_diff > 0 else -1
            )
            pos = row, col

            for i in range(1, abs(col_diff)):
                pos = (
                pos[0] + dir[0],
                pos[1] + dir[1]
                )

                if board.chessboard[pos[0]][pos[1]] != None:
                    return False
            return True
        elif target_col == col and (target_row in range(8)) and (board.chessboard[target_row][target_col] == None or board.chessboard[target_row][target_col].color != board.chessboard[row][col].color):
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

                if board.chessboard[pos[0]][pos[1]] != None:
                    return False
            return True
        else:
            return False
