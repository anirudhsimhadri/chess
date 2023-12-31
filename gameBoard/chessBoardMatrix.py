"""
Two Player Lan Chess
By: Sam Aven, Ani Simhadri, Andrew Voss
This project was created during an intership with PRI Global
Purpose of this file: Handles the physical chessboard and loading/placing the imgaes for the pieces
"""
import pygame
import sys
from BoardConstants import BoardConstants
from typedef import ChessPiece, unwrap, ChessBoardMatrix as Cbm
from typing import cast
Surface = pygame.Surface

class ChessBoardMatrix:
    chessboard: list[list[ChessPiece | None]]

    def __init__(self, is_client: bool):
        #define the rows and columns of the matrix
        self.rows = 8
        self.cols = 8

        self.chessboard = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        
        if is_client:
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
    
    def is_king_in_check(self, color: str) -> bool:
        king_pos = (99, 99) # obvious dummy value

        for row in range(8):
            for col in range(8):
                piece = self.chessboard[row][col]

                if piece is not None and piece.pieceType == "king" and piece.color == color:
                    king_pos = (row, col)
                    break
        
        assert king_pos != (99, 99), f"Couldn't find {color} king"
        
        for row in range(8):
            for col in range(8):
                piece = self.chessboard[row][col]
                # Hacky way to get around incomplete move validation
                if piece is not None and callable(getattr(piece, "is_valid_move", None)):
                    if piece.is_valid_move(row, col, *king_pos, cast(Cbm, self)):
                        return True
        
        return False
    
    def is_threatened(self, row, col, color) -> bool:
        for row_ in range(8):
            for col_ in range(8):
                piece = self.chessboard[row_][col_]
                # Hacky way to get around incomplete move validation
                if piece is not None and piece.color != color and callable(getattr(piece, "is_valid_move", None)):
                    if piece.is_valid_move(row_, col_, row, col, cast(Cbm, self)):
                        return True
        
        return False
    
    def is_checkmate(self, color: str) -> bool:
        if not self.is_king_in_check(color): return False
        
        for row in range(self.rows):
            for col in range(self.cols):
                piece = self.chessboard[row][col]
                if piece is not None and piece.color == color:
                    if callable(getattr(piece, "all_valid_moves", None)):
                        for move in piece.all_valid_moves(row, col, cast(Cbm, self)):
                            target = self.chessboard[move[0]][move[1]]
                            self.move(row, col, *move)

                            check = self.is_king_in_check(color)

                            self.undo_move(row, col, *move, target)

                            if not check: return False
        
        return True
    
    def move(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
    ):
        """Does the heavy lifting for actually moving pieces"""
        piece = self.chessboard[start_row][start_col]
        assert piece is not None

        print(f"Move {piece.pieceType} from {(start_row, start_col)} to {(end_row, end_col)}")
        
        if piece.pieceType == "pawn":
            piece.hasMoved = True

        if (
            piece.pieceType == "king"
            and not piece.hasMoved
            and (
                end_col == 2
                or end_col == 6
            )
        ):
            assert start_row == end_row

            if end_col == 2:
                rook = self.chessboard[start_row][0]
                assert rook is not None
                assert not rook.hasMoved

                self.chessboard[start_row][2] = piece
                self.chessboard[start_row][4] = None
                self.chessboard[start_row][3] = rook
                self.chessboard[start_row][0] = None

                rook.hasMoved = True
            else:
                assert end_col == 6
                rook = self.chessboard[start_row][7]
                assert rook is not None
                assert not rook.hasMoved

                self.chessboard[start_row][6] = piece
                self.chessboard[start_row][4] = None
                self.chessboard[start_row][5] = rook
                self.chessboard[start_row][7] = None

                rook.hasMoved = True

            piece.hasMoved = True

            return
        
        self.chessboard[end_row][end_col] = self.chessboard[start_row][start_col]
        self.chessboard[start_row][start_col] = None
    
    def undo_move(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
        captured_piece: ChessPiece | None
    ):
        """inverse to `move()`"""
        piece = self.chessboard[end_row][end_col]
        assert piece is not None

        self.chessboard[start_row][start_col] = piece
        self.chessboard[end_row][end_col] = captured_piece

    def draw_pieces(self, screen: Surface):
        for row in range(self.rows):
            for col in range(self.cols):
                piece = self.chessboard[row][col]
                if piece:
                    x = (col * self.cs.SQUARE_SIZE + self.cs.OFFSET_X + 5)
                    y = (row * self.cs.SQUARE_SIZE + self.cs.OFFSET_Y + 5)
                    
                    if piece == None:
                        continue
                    else:
                        if piece.pieceType == 'pawn':
                            screen.blit(unwrap(self.pawn_images.get(piece.color)), (x, y))
                        elif piece.pieceType == 'rook':
                            screen.blit(unwrap(self.rook_images.get(piece.color)), (x, y))
                        elif piece.pieceType == 'bishop':
                            screen.blit(unwrap(self.bishop_images.get(piece.color)), (x, y))
                        elif piece.pieceType == 'queen':
                            screen.blit(unwrap(self.queen_images.get(piece.color)), (x, y))
                        elif piece.pieceType == 'king':
                            screen.blit(unwrap(self.king_images.get(piece.color)), (x, y))
                        elif piece.pieceType == 'knight':
                            screen.blit(unwrap(self.knight_images.get(piece.color)), (x, y))
                    
    #create screen
    def draw_chessboard(self, screen: Surface):
        for row in range(8):
            for col in range(8):
                color = self.cs.LIGHT_BROWN if (row + col) % 2 == 0 else self.cs.DARK_BROWN
                pygame.draw.rect(screen, color, (col * self.cs.SQUARE_SIZE + self.cs.OFFSET_X, row * self.cs.SQUARE_SIZE + self.cs.OFFSET_Y, self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))