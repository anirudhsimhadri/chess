import pygame
from BoardConstants import BoardConstants

class Knight():
    def __init__(self, color:str):
        self.type = "knight"
        self.color = color
        self.MaterialValue = 3

        if self.color == "white":
            self.image = pygame.image.load('white_knight.png').convert_alpha()
        elif self.color == "black":
            self.image = pygame.image.load('black_knight.png').convert_alpha()
        
        self.cs = BoardConstants()

        self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))

    def move(self, x, y):
        """Knight move funtion"""