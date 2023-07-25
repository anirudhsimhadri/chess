import pygame
import sys
from chessBoardMatrix import ChessBoardMatrix
from BoardConstants import BoardConstants
import chessPieces.pawn as p
Surface = pygame.Surface

pygame.init()
cs = BoardConstants()

def draw_tracking_boxes(screen: Surface):
    """Draws the material tracking boxes on the screen"""

    #top tracking box
    pygame.draw.rect(screen, cs.BLUE, (cs.OFFSET_X, 0, cs.BOX_WIDTH, cs.BOX_HEIGHT))

    #bottom tracking box
    pygame.draw.rect(screen, cs.BLUE, (cs.OFFSET_X, cs.WINDOW_SIZE - cs.BOX_HEIGHT, cs.BOX_WIDTH, cs.BOX_HEIGHT))
        
def draw_border(screen: Surface):
    """Draws the border around the important screen elements"""
    pygame.draw.rect(screen, cs.BLACK, (cs.OFFSET_X, cs.OFFSET_Y, cs.BOARD_SIZE, cs.BOARD_SIZE), 5)
    pygame.draw.rect(screen, cs.BLACK, (cs.OFFSET_X- 4, cs.OFFSET_Y - 150, cs.BOX_WIDTH + 8, cs.BOX_HEIGHT + 8), 5)
    pygame.draw.rect(screen, cs.BLACK, (cs.OFFSET_X - 4, cs.OFFSET_Y + cs.BOARD_SIZE, cs.BOX_WIDTH + 8, cs.BOX_HEIGHT + 8), 5)

def main():
    screen = pygame.display.set_mode((cs.WINDOW_SIZE, cs.WINDOW_SIZE))
    pygame.display.set_caption("Chess Board")

    chessboard_matrix = ChessBoardMatrix()

    # Place white pawns ('P') on row 1
    for col in range(chessboard_matrix.cols):
        chessboard_matrix.place_piece(1, col, 'P')

    # Place black pawns ('p') on row 6
    for col in range(chessboard_matrix.cols):
        chessboard_matrix.place_piece(6, col, 'p')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #fill the screen edges
        screen.fill(cs.RED)

        #Draw the chessboard
        chessboard_matrix.draw_chessboard(screen)

        #Draw the pieces
        chessboard_matrix.draw_pieces(screen)

        #Draw the material tracking boxes
        draw_tracking_boxes(screen)

        #Draw the border around the chessboard
        draw_border(screen)

        #Update the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()