import pygame
from BoardConstants import BoardConstants

class Rook():
    def __init__(self, color:str):
        self.type = "rook"
        self.color = color
        self.MaterialValue = 5

        if self.color == "white":
            self.image = pygame.image.load('white_rook.png').convert_alpha()
        elif self.color == "black":
            self.image = pygame.image.load('black_rook.png').convert_alpha()
        
        self.cs = BoardConstants()

        self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))
    
    def move(self, x, y):
        """Rook move funtion"""