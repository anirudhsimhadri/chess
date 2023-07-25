class BoardConstants():
    def __init__(self):
        
        self.BOARD_SIZE = 400
        self.SQUARE_SIZE = self.BOARD_SIZE // 8

        #window dimentions
        self.WINDOW_SIZE = 700

        #offset for chess board
        self.OFFSET_Y = (self.WINDOW_SIZE - self.BOARD_SIZE) // 2
        self.OFFSET_X = 0

        #Calculate the dimensions and positions of the material tracking boxes
        self.BOX_WIDTH = self.SQUARE_SIZE * 8
        self.BOX_HEIGHT = (self.WINDOW_SIZE - self.BOARD_SIZE) // 2

        #define colors
        self.LIGHT_BROWN = (181, 101, 29)
        self.DARK_BROWN = (89, 49, 11)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)