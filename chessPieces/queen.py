import pygame
from BoardConstants import BoardConstants

class Queen():
    def __init__(self, color:str):
        self.type = "queen"
        self.color = color
        self.MaterialValue = 9

        if self.color == "white":
            self.image = pygame.image.load('white_queen.png').convert_alpha()
        elif self.color == "black":
            self.image = pygame.image.load('black_queen.png').convert_alpha()
        
        self.cs = BoardConstants()

        self.image = pygame.transform.scale(self.image, (self.cs.SQUARE_SIZE, self.cs.SQUARE_SIZE))

    def move(self, x, y):
        """Queen move function"""