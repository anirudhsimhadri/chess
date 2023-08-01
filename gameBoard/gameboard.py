import pygame
import sys
from chessBoardMatrix import ChessBoardMatrix
from BoardConstants import BoardConstants
from pawn import Pawn as p
from bishop import Bishop as b
from rook import Rook as r
from knight import Knight as k
from queen import Queen as q
from king import King
from typedef import ChessPiece, ChessBoardMatrix as Cbm
from typing import cast
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

    #chessboard bounds
    pygame.draw.rect(screen, cs.BLACK, (cs.OFFSET_X, cs.OFFSET_Y, cs.BOARD_SIZE, cs.BOARD_SIZE), 5)
    #pygame.draw.rect(screen, cs.BLACK, (cs.OFFSET_X- 4, cs.OFFSET_Y - 150, cs.BOX_WIDTH + 8, cs.BOX_HEIGHT + 8), 5)
    #pygame.draw.rect(screen, cs.BLACK, (cs.OFFSET_X - 4, cs.OFFSET_Y + cs.BOARD_SIZE, cs.BOX_WIDTH + 8, cs.BOX_HEIGHT + 8), 5)


def main():
    screen = pygame.display.set_mode((cs.WINDOW_SIZE, cs.WINDOW_SIZE))
    pygame.display.set_caption("Chess Board")

    chessboard_matrix = ChessBoardMatrix()

    white_pawn = p('white')
    black_pawn = p('black')

    # Place white pawns ('P') on row 6
    for col in range(chessboard_matrix.cols):
        chessboard_matrix.place_piece(6, col, white_pawn)

    # Place black pawns ('p') on row 1
    for col in range(chessboard_matrix.cols):
        chessboard_matrix.place_piece(1, col, black_pawn)
    
    #place Rooks
    black_rook = r('black')
    white_rook = r('white')
    chessboard_matrix.place_piece(0, 0, black_rook)
    chessboard_matrix.place_piece(7, 7, white_rook)
    chessboard_matrix.place_piece(0, 7, black_rook)
    chessboard_matrix.place_piece(7, 0, white_rook)

    #place Bishops
    black_bishop = b('black')
    white_bishop = b('white')
    chessboard_matrix.place_piece(0, 1, black_bishop)
    chessboard_matrix.place_piece(7, 6, white_bishop)
    chessboard_matrix.place_piece(0, 6, black_bishop)
    chessboard_matrix.place_piece(7, 1, white_bishop)
    
    #place Knights
    black_knight = k('black')
    white_knight = k('white')
    chessboard_matrix.place_piece(0, 2, black_knight)
    chessboard_matrix.place_piece(7, 5, white_knight)
    chessboard_matrix.place_piece(0, 5, black_knight)
    chessboard_matrix.place_piece(7, 2, white_knight)
    
    #place Queens
    black_queen = q('black')
    white_queen = q('white')
    chessboard_matrix.place_piece(0, 3, black_queen)
    chessboard_matrix.place_piece(7, 3, white_queen)

    #place Kings
    black_king = King('black')
    white_king = King('white')
    chessboard_matrix.place_piece(0, 4, black_king)
    chessboard_matrix.place_piece(7, 4, white_king)

    selected_square: tuple[int, int] | None = None
    selected_piece: ChessPiece | None = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    clicked_row, clicked_col = (mouse_y - cs.OFFSET_Y) // cs.SQUARE_SIZE, mouse_x // cs.SQUARE_SIZE
                    if clicked_row >= 8 or clicked_col >= 8 or clicked_row < 0 or clicked_col < 0:
                        selected_square = None
                    else:
                        if selected_square is None:
                            selected_square = (clicked_row, clicked_col)
                            print(selected_square)
                            selected_piece = chessboard_matrix.chessboard[selected_square[0]][selected_square[1]]
                            if selected_piece == None:
                                selected_square = None
                            
                        else:
                            assert selected_piece is not None

                            target = chessboard_matrix.chessboard[clicked_row][clicked_col]
                            print(target)

                            if selected_piece.is_valid_move(*selected_square, clicked_row, clicked_col, cast(Cbm, chessboard_matrix)):
                                chessboard_matrix.move(*selected_square, clicked_row, clicked_col)
                            
                            if chessboard_matrix.is_king_in_check(selected_piece.color):
                                chessboard_matrix.undo_move(*selected_square, clicked_row, clicked_col, target)
                            
                            def inverse_color(color: str) -> str:
                                return "black" if color == "white" else "white"
                            
                            opp_color = inverse_color(selected_piece.color)

                            if chessboard_matrix.is_checkmate(opp_color):
                                print(f"checkmate for {opp_color}")

                            #clear the selected square
                            selected_square = None
                            selected_piece = None
                            
        
        #fill the screen edges
        screen.fill(cs.BLACK)

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