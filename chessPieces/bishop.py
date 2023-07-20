from chesspiece import ChessPiece

class Bishop(ChessPiece):
    def __init__(self, color:str):
        super().__init__("bishop", color,3)

    def move(self, x, y):
        """Bishop move function"""
