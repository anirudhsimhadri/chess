from chesspiece import ChessPiece

class King(ChessPiece):
    def __init__(self, color:str):
        super().__init__("king", color, 100)
    
    def move(self, x, y):
        """Kings move funtion"""
    
    def castle(self, x, y):
        """Kings castle funtion"""
        