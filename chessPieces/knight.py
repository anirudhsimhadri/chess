from chesspiece import Chesspieces

class Knight(Chesspieces):
    def __init__(self, color:str):
        super().__init__("knight", color, 3)

    def move(self, x, y):
        """Knight move funtion"""