import pygame
from BoardConstants import BoardConstants

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
        self.hasMoved = True #set to True so the pawn cant move two squares forward
    def is_valid_move(self, board, new_x, new_y):
        """
        Checks if the move is valid (it's a straight line and no piece is blocking the path).
        This doesn't check if the king would be in check after this move - that logic belongs elsewhere.
        """
        if new_x != self.x and new_y != self.y:  # The rook moves in a straight line
            return False

        # check if there's any piece blocking the way
        if new_x == self.x:  # moving vertically
            for y in range(min(self.y, new_y) + 1, max(self.y, new_y)):
                if board[self.x][y] != 0:  # there's a piece in the way
                    return False
        else:  # moving horizontally
            for x in range(min(self.x, new_x) + 1, max(self.x, new_x)):
                if board[x][self.y] != 0:  # there's a piece in the way
                    return False

        # if we're here, then no piece is blocking the way. Now we need to check the destination
        if board[new_x][new_y] == 1:  # we're moving to a space occupied by a friendly piece
            return False

        # if we're here, then all conditions have been satisfied
        return True
