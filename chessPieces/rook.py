from chesspiece import ChessPiece

class Rook(ChessPiece):
    def __init__(self, color:str):
        super().__init__("rook", color, 5)
    
    def move(self, x, y):
        """Rook move funtion"""