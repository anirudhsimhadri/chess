import pygame
import sys

pygame.init()

#dimensions of chessboard and size of each square
#WIDTH, HEIGHT = 700, 700
#SQUARE_SIZE = WIDTH // 8

BOARD_SIZE = 650
SQUARE_SIZE = BOARD_SIZE // 8

#window dimentions
WINDOW_SIZE = 900

#offset for chess board
OFFSET_Y = (WINDOW_SIZE - BOARD_SIZE) // 2
OFFSET_X = 0

#Calculate the dimensions and positions of the material tracking boxes
BOX_WIDTH = SQUARE_SIZE * 8
BOX_HEIGHT = (WINDOW_SIZE - BOARD_SIZE) // 2

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class ChessboardMatrix:
    def __init__(self):
        #define the rows and columns of the matrix
        self.rows = 8
        self.cols = 8

        self.chessboard = [['-'for _ in range(self.cols)] for _ in range(self.rows)]

    def place_piece(self, row, col, piece):
        self.chessboard[row][col] = piece

    def draw_piece(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                piece = self.chessboard[row][col]
                if piece != '-':
                    x = col * SQUARE_SIZE + OFFSET_X + SQUARE_SIZE // 2
                    y = row * SQUARE_SIZE + OFFSET_Y + SQUARE_SIZE // 2
                    font = pygame.font.SysFont('Arial', 30)
                    text_surface = font.render(piece, True, RED)
                    text_rect = text_surface.get_rect(center=(x, y))
                    screen.blit(text_surface, text_rect)
    
    #create screen
    def draw_chessboard(self, screen):
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE + OFFSET_X, row * SQUARE_SIZE + OFFSET_Y, SQUARE_SIZE, SQUARE_SIZE))


def draw_tracking_boxes(screen):
    """Draws the material tracking boxes on the screen"""

    #top tracking box
    pygame.draw.rect(screen, BLUE, (OFFSET_X, 0, BOX_WIDTH, BOX_HEIGHT))

    #bottom tracking box
    pygame.draw.rect(screen, BLUE, (OFFSET_X, WINDOW_SIZE - BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT))
        
def draw_border(screen):
    """Draws the border around the important screen elements"""
    pygame.draw.rect(screen, BLACK, (OFFSET_X, OFFSET_Y, BOARD_SIZE, BOARD_SIZE), 5)
    pygame.draw.rect(screen, BLACK, (OFFSET_X- 4, OFFSET_Y - 130, BOX_WIDTH + 8, BOX_HEIGHT + 8), 5)
    pygame.draw.rect(screen, BLACK, (OFFSET_X - 4, OFFSET_Y + BOARD_SIZE, BOX_WIDTH + 8, BOX_HEIGHT + 8), 5)

def main():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Chess Board")

    chessboard_matrix = ChessboardMatrix()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #fill the screen edges
        screen.fill(RED)

        #Draw the chessboard
        chessboard_matrix.draw_chessboard(screen)

        #Draw the pieces
        chessboard_matrix.draw_piece(screen)

        #Draw the material tracking boxes
        draw_tracking_boxes(screen)

        #Draw the border around the chessboard
        draw_border(screen)

        #Update the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()