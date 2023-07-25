from chesspiece import ChessPiece

class Bishop(ChessPiece):
    def __init__(self, color:str):
        super().__init__("bishop", color,3)

    def valid_move(self, start_row, start_col, end_row, end_col) -> bool:
        row_diff = end_row - start_row
        col_diff = abs(end_col - start_col)

        return abs(row_diff) == abs(col_diff)
