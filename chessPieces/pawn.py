from chesspiece import ChessPiece

class Pawn(ChessPiece):
    def __init__(self, color:str, hasMoved:bool):
        super().__init__("pawn", color,1)
        self.hasMoved = False
    
    def __str__(self):
        return "pawn" if self.color == "white" else "p"
    
    def valid_move(self, start_row, start_col, end_row, end_col, is_capture):
        direction = 1 if self.color == "white" else -1
        row_diff = end_row - start_row
        col_diff = abs(end_col - start_col)

        if is_capture:
            #Pawn capturing diagonally
            return row_diff == direction and col_diff == 1
        else:
            if not self.hasMoved:
                #First move pawns may move two squares forward
                return (row_diff == 2 * direction or row_diff == direction) and col_diff == 0
            else:
                return row_diff == direction and col_diff == 0

    def en_pessant(self, x, y):
        """"pawn en pessant capability"""
        