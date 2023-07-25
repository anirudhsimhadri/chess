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
            'white': pygame.image.load('white_pawn.png').convert_alpha(),
            'black': pygame.image.load('black_pawn.png').convert_alpha()
        }
        self.rook_images ={
            'white': pygame.image.load('white_rook.png').convert_alpha(),
            'black': pygame.image.load('black_rook.png').convert_alpha()
        }
        self.bishop_images ={
            'white': pygame.image.load('white_bishop.png').convert_alpha(),
            'black': pygame.image.load('black_bishop.png').convert_alpha()
        }
        self.queen_images ={
            'white': pygame.image.load('white_queen.png').convert_alpha(),
            'black': pygame.image.load('black_queen.png').convert_alpha()
        }
        self.king_images ={
            'white': pygame.image.load('white_king.png').convert_alpha(),
            'black': pygame.image.load('black_king.png').convert_alpha()
        }
        self.knight_images ={
            'white': pygame.image.load('white_knight.png').convert_alpha(),
            'black': pygame.image.load('black_knight.png').convert_alpha()
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
                    
                    if self.pawn_images.get(piece) is not None:
                        screen.blit(self.pawn_images.get(piece), (x, y))

    
    #create screen
    def draw_chessboard(self, screen: Surface):
        for row in range(8):
            for col in range(8):
                color = self.cs.LIGHT_BROWN if (row + col) % 2 == 0 else self.cs.DARK_BROWN
                pygame.draw.rect(screen, color, (col * self.cs.SQUARE_SIZE + self.cs.OFFSET_X, row * self.cs.SQUARE_SIZE + self.cs.OFFSET_Y, self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))