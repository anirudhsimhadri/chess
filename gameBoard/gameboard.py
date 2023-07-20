import pygame
import sys

pygame.init()

#dimensions of chessboard and size of each square
#WIDTH, HEIGHT = 700, 700
#SQUARE_SIZE = WIDTH // 8

BOARD_SIZE = 600
SQUARE_SIZE = BOARD_SIZE // 8

#window dimentions
WINDOW_SIZE = 900

#offset for chess board
OFFSET_Y = (WINDOW_SIZE - BOARD_SIZE) // 2
OFFSET_X = 0

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#create screen
def draw_chessboard(screen):
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE + OFFSET_X, row * SQUARE_SIZE + OFFSET_Y, SQUARE_SIZE, SQUARE_SIZE))

def main():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Chess Board")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #Clear the screen
        screen.fill(RED)

        #Draw the chessboard
        draw_chessboard(screen)

        #Update the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()