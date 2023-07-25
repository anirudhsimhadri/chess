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
        self.cs = BoardConstants()

    def place_piece(self, row, col, piece):
        self.chessboard[row][col] = piece


    """def draw_piece(self, screen: Surface):
        for row in range(self.rows):
            for col in range(self.cols):
                piece = self.chessboard[row][col]
                if piece != '-':
                    x = col * SQUARE_SIZE + OFFSET_X + SQUARE_SIZE // 2
                    y = row * SQUARE_SIZE + OFFSET_Y + SQUARE_SIZE // 2
                    font = pygame.font.SysFont('Arial', 30)
                    text_surface = font.render(piece, True, RED)
                    text_rect = text_surface.get_rect(center=(x, y))
                    screen.blit(text_surface, text_rect)"""

    def draw_pieces(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                piece = self.chessboard[row][col]
                x = col * self.cs.SQUARE_SIZE + self.cs.OFFSET_X + self.cs.SQUARE_SIZE // 2
                y = row * self.cs.SQUARE_SIZE + self.cs.OFFSET_Y + self.cs.SQUARE_SIZE // 2
                if piece == 'P' or piece == 'p':
                    font = pygame.font.SysFont('Arial', 30)
                    text_surface = font.render(piece, True, self.cs.BLACK)
                    text_rect = text_surface.get_rect(center=(x, y))
                    screen.blit(text_surface, text_rect)
    #create screen
    def draw_chessboard(self, screen: Surface):
        for row in range(8):
            for col in range(8):
                color = self.cs.LIGHT_BROWN if (row + col) % 2 == 0 else self.cs.DARK_BROWN
                pygame.draw.rect(screen, color, (col * self.cs.SQUARE_SIZE + self.cs.OFFSET_X, row * self.cs.SQUARE_SIZE + self.cs.OFFSET_Y, self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))