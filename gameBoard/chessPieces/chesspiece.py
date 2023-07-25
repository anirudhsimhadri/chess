class ChessPiece:
    def __init__(self, name:str, color:str, MaterialValue:int):
        self.name:str = None
        self.color:str = None
        self.MaterialValue:int = 0
    
    def move(self):
        """Move the piece to the next user selected position"""
    