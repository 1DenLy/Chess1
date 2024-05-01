import pygame


class Cell():

    def __init__(self, statusCell: bool = False, pixelPosition_X: int = 0, pixelPosition_Y: int = 0, cellColor: bool = True, rowPosition: str = None, colPosition: str = None):

        
        self.rect = pygame.Rect(pixelPosition_X, pixelPosition_Y, 80, 80)
        
        self.active = statusCell 

        self.pixelPosition_X = pixelPosition_X
        self.pixelPosition_Y = pixelPosition_Y

        self.rowPosition = rowPosition
        self.colPosition = colPosition

        self.figureOn = None

        if cellColor:
            self.cellColor = (210, 210, 210) # WHITE
        else:
            self.cellColor = (0, 56, 34) # BLACK


    def draw(self, surface: pygame.Surface) -> pygame.Surface:
        pygame.draw.rect(surface, self.cellColor, self.rect)

