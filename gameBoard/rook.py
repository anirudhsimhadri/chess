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
    
    def move(self, row, col, target_row, target_col):
        self.row = target_row
        self.col = target_col
        self.hasMoved = True
        """
        Checks if the move is valid (it's a straight line and no piece is blocking the path).
        This doesn't check if the king would be in check after this move - that logic belongs elsewhere.
        """
        if new_x != self.x and new_y != self.y:  # The rook moves in a straight line
            return False

        # check if there's any piece blocking the way
        if new_x == x:  # moving vertically
            for y in range(min(y, new_y) + 1, max(y, new_y)):
                if board.chessboard[x][y] != 0:  # there's a piece in the way
                    return False
        else:  # moving horizontally
            for x in range(min(x, new_x) + 1, max(x, new_x)):
                if board.chessboard[x][y] != 0:  # there's a piece in the way
                    return False

        # if we're here, then no piece is blocking the way. Now we need to check the destination
        if board.chessboard[new_x][new_y] == 1:  # we're moving to a space occupied by a friendly piece
            return False

        # if we're here, then all conditions have been satisfied
        return True
    
        """if new_x == x and (new_y in range(8)) and (board.chessboard[new_x][new_y] == None or board.chessboard[new_x][new_y].color != board.chessboard[x][y].color):
            return True
        elif new_y == y and (new_x in range(8)) and (board.chessboard[new_x][new_y] == None or board.chessboard[new_x][new_y].color != board.chessboard[x][y].color):
            return True
        else:
            return False"""
