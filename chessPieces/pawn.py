from chesspiece import ChessPiece

class Pawn(ChessPiece):
    def __init__(self, color:str):
        super().__init__("pawn", color,1)
    
    def move(self, x, y):
        """Pawn move function"""

    def en_pessant(self, x, y):
        """"pawn en pessant capability"""
        