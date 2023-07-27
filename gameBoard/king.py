import pygame
from BoardConstants import BoardConstants

class King():
    def __init__(self, color:str):
        self.pieceType = "king"
        self.color = color
        self.MaterialValue = 99
        self.hasMoved = False

        if self.color == "white":
            self.image = pygame.image.load('white_king.png').convert_alpha()
        elif self.color == "black":
            self.image = pygame.image.load('black_king.png').convert_alpha()
        
        self.cs = BoardConstants()

        self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))
    
    def move(self, x, y):
        """Kings move funtion"""
    
    def castle(self, x, y):
        """Kings castle funtion"""
        