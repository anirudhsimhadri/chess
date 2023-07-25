import pygame
import sys
from BoardConstants import BoardConstants
Surface = pygame.Surface

class ChessBoardMatrix:
    def __init__(self):
        #define the rows and columns of the matrix
        self.rows = 8
        self.cols = 8

        self.chessboard = [['-'for _ in range(self.cols)] for _ in range(self.rows)]
        
        #load images
        self.pawn_images ={
            'P': pygame.image.load('chess/1x/w_pawn_1x.png'),
            'p': pygame.image.load('chess/1x/b_pawn_1x.png')
        }

        self.cs = BoardConstants()

    def place_piece(self, row, col, piece):
        self.chessboard[row][col] = piece

    def draw_pieces(self, screen: Surface):
        for row in range(self.rows):
            for col in range(self.cols):
                piece = self.chessboard[row][col]
                if piece:
                    x = (col * self.cs.SQUARE_SIZE + self.cs.OFFSET_X)
                    y = (row * self.cs.SQUARE_SIZE + self.cs.OFFSET_Y)
                    screen.blit(self.pawn_images[piece], (x, y))

    
    #create screen
    def draw_chessboard(self, screen: Surface):
        for row in range(8):
            for col in range(8):
                color = self.cs.LIGHT_BROWN if (row + col) % 2 == 0 else self.cs.DARK_BROWN
                pygame.draw.rect(screen, color, (col * self.cs.SQUARE_SIZE + self.cs.OFFSET_X, row * self.cs.SQUARE_SIZE + self.cs.OFFSET_Y, self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))