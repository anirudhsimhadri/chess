from chesspiece import ChessPiece

class Queen(ChessPiece):
    def __init__(self, color:str):
        super().__init__("queen", color, 9)

    def move(self, x, y):
        """Queen move function"""