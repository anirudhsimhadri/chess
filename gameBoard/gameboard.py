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
from socket import socket as Socket
import resultscreen as rs
import net
Surface = pygame.Surface

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

def draw_validation_popup(screen: Surface, msg: str):
    """Draws the message when you make an invalid move"""

    font = pygame.font.SysFont("Arial", 18)
    text = font.render(msg, True, (0xff, 0xff, 0xff))
    screen.blit(text, (cs.BOARD_SIZE + 18, cs.BOARD_SIZE // 3))

def main(conn: Socket | None, is_white: bool):
    screen = pygame.display.set_mode((cs.WINDOW_SIZE, cs.WINDOW_SIZE))
    pygame.display.set_caption("Chess Board")

    chessboard_matrix = ChessBoardMatrix(True)


    # Place white pawns ('P') on row 6
    for col in range(chessboard_matrix.cols):
        chessboard_matrix.place_piece(6, col, p("white"))

    # Place black pawns ('p') on row 1
    for col in range(chessboard_matrix.cols):
        chessboard_matrix.place_piece(1, col, p("black"))

    # Piece types and their corresponding columns
    pieces = [
        (r, [0, 7]), (b, [1, 6]), (k, [2, 5]),
        (q, [3]), (King, [4])
    ]

    # Iterate through piece types and columns
    for piece, cols in pieces:
        for col in cols:
            func = piece if piece != King else King
            chessboard_matrix.place_piece(0, col, func('black'))
            chessboard_matrix.place_piece(7, col, func('white'))

    # #place Rooks
    # chessboard_matrix.place_piece(0, 0, r("black"))
    # chessboard_matrix.place_piece(7, 7, r("white"))
    # chessboard_matrix.place_piece(0, 7, r("black"))
    # chessboard_matrix.place_piece(7, 0, r("white"))

    # #place Bishops
    # chessboard_matrix.place_piece(0, 1, b("black"))
    # chessboard_matrix.place_piece(7, 6, b("white"))
    # chessboard_matrix.place_piece(0, 6, b("black"))
    # chessboard_matrix.place_piece(7, 1, b("white"))
    
    # #place Knights
    # chessboard_matrix.place_piece(0, 2, k('black'))
    # chessboard_matrix.place_piece(7, 5, k('white'))
    # chessboard_matrix.place_piece(0, 5, k('black'))
    # chessboard_matrix.place_piece(7, 2, k('white'))
    
    # #place Queens
    # chessboard_matrix.place_piece(0, 3, q('black'))
    # chessboard_matrix.place_piece(7, 3, q('white'))

    # #place Kings
    # chessboard_matrix.place_piece(0, 4, King('black'))
    # chessboard_matrix.place_piece(7, 4, King('white'))

    selected_square: tuple[int, int] | None = None
    selected_piece: ChessPiece | None = None

    opponents_move = not is_white
    first_move = True
    did_win: bool | None = None
    validation_message: str | None = None

    while True:
        if not opponents_move:
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

                                if conn is None: # Server can handle all this
                                    if selected_piece.is_valid_move(*selected_square, clicked_row, clicked_col, cast(Cbm, chessboard_matrix)):
                                        chessboard_matrix.move(*selected_square, clicked_row, clicked_col)
                                    
                                        if chessboard_matrix.is_king_in_check(selected_piece.color):
                                            chessboard_matrix.undo_move(*selected_square, clicked_row, clicked_col, target)
                                    
                                        opp_color = "white" if selected_piece.color == "black" else "black"

                                        if chessboard_matrix.is_checkmate(opp_color):
                                            print(f"checkmate for {opp_color}")
                                else:
                                    net.sendMove(conn, selected_square, (clicked_row, clicked_col))
                                    print("Sent move")

                                    response = conn.recv(8)
                                    print(response)

                                    if response == b"valid!!!":
                                        chessboard_matrix.move(*selected_square, clicked_row, clicked_col)
                                        validation_message = None
                                        opponents_move = True
                                    elif response == b"gameover":
                                        chessboard_matrix.move(*selected_square, clicked_row, clicked_col)
                                        validation_message = None
                                        did_win = True
                                    else: # Move was invalid, let's see why
                                        if response == b"invalid!" and selected_square != (clicked_row, clicked_col):
                                            validation_message = f"{selected_piece.pieceType.title()} cannot move in that way"
                                        elif response == b"check!!!":
                                            validation_message = "King is in check"
                                        elif response == b"pinned!!":
                                            validation_message = f"{selected_piece.pieceType.title()} is pinned"
                                #clear the selected square
                                selected_square = None
                                selected_piece = None
                            
        elif conn is not None and not first_move:
            start, end = net.recvMove(conn)
            print("received move")
            chessboard_matrix.move(*start, *end)
            message = conn.recv(8)
            print(message)
            
            if message == b"gameover":
                did_win = False
            else:
                assert message == b"yourmove"
            opponents_move = False
        
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

        if validation_message is not None:
            draw_validation_popup(screen, validation_message)

        if did_win is not None:
            rs.draw_result_screen(screen, did_win)

        #Update the screen
        pygame.display.flip()

        first_move = False

if __name__ == "__main__":
    pygame.init()
    main(None, True)
