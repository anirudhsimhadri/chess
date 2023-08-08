"""
Two Player Lan Chess
By: Sam Aven, Ani Simhadri, Andrew Voss
This project was created during an intership with PRI Global
Purpose of this file: Handles all queen functionality
"""
import pygame
from BoardConstants import BoardConstants
from chessBoardMatrix import ChessBoardMatrix as cbm

class Queen():
    def __init__(self, color:str):
        self.pieceType = "queen"
        self.color = color
        self.MaterialValue = 9

        #if self.color == "white":
        #    self.image = pygame.image.load('white_queen.png').convert_alpha()
        #elif self.color == "black":
        #    self.image = pygame.image.load('black_queen.png').convert_alpha()
        
        self.cs = BoardConstants()

        #self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))

    def is_valid_move(self, start_row, start_col, end_row, end_col, matrix:cbm):
        """Queen move function"""
        return self.is_valid_move_diagonally(start_row, start_col, end_row, end_col, matrix) or self.is_valid_move_up_down_left_right(start_row, start_col, end_row, end_col, matrix)

    def is_valid_move_diagonally(self, start_row, start_col, end_row, end_col, matrix: cbm) -> bool:
        row_diff = end_row - start_row
        col_diff = end_col - start_col
        # Check if the queen can move to the target location
        delta_row = end_row - start_row
        delta_col = end_col - start_col

        # Queen moves along a rank, file, or diagonal
        # if abs(delta_row) == abs(delta_col) or start_row == end_row or start_col == end_col:
        #     # Check if the path is clear
        #     path_rows = range(start_row + delta_row//abs(delta_row), end_row, delta_row//abs(delta_row)) if delta_row != 0 else [start_row]*abs(delta_col)
        #     path_cols = range(start_col + delta_col//abs(delta_col), end_col, delta_col//abs(delta_col)) if delta_col != 0 else [start_col]*abs(delta_row)
        #     for r, c in zip(path_rows, path_cols):
        #         if matrix.chessboard[r][c]:
        #             return False
        #     return True
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
        return False

    def is_valid_move_up_down_left_right(self, row, col, target_row, target_col, board):
        """
        Checks if the move is valid (it's a straight line and no piece is blocking the path).
        This doesn't check if the king would be in check after this move - that logic belongs elsewhere.
        """
        row_diff = target_row - row
        col_diff = target_col - col


        if target_row == row and (target_col in range(8)) and (board.chessboard[target_row][target_col] == None or board.chessboard[target_row][target_col].color != board.chessboard[row][col].color):
            dir = (
            0,
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
            0
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