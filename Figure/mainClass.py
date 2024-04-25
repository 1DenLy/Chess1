import pygame

# Инициализация Pygame
pygame.init()

Cells_coordinate = {
    'A1': (10, 10),  'B1': (90, 10),  'C1': (170, 10),  'D1': (250, 10),  'E1': (330, 10),  'F1': (410, 10),  'G1': (490, 10),  'H1': (570, 10),
    'A2': (10, 90),  'B2': (90, 90),  'C2': (170, 90),  'D2': (250, 90),  'E2': (330, 90),  'F2': (410, 90),  'G2': (490, 90),  'H2': (570, 90),
    'A3': (10, 170), 'B3': (90, 170), 'C3': (170, 170), 'D3': (250, 170), 'E3': (330, 170), 'F3': (410, 170), 'G3': (490, 170), 'H3': (570, 170),
    'A4': (10, 250), 'B4': (90, 250), 'C4': (170, 250), 'D4': (250, 250), 'E4': (330, 250), 'F4': (410, 250), 'G4': (490, 250), 'H4': (570, 250),
    'A5': (10, 330), 'B5': (90, 330), 'C5': (170, 330), 'D5': (250, 330), 'E5': (330, 330), 'F5': (410, 330), 'G5': (490, 330), 'H5': (570, 330),
    'A6': (10, 410), 'B6': (90, 410), 'C6': (170, 410), 'D6': (250, 410), 'E6': (330, 410), 'F6': (410, 410), 'G6': (490, 410), 'H6': (570, 410),
    'A7': (10, 490), 'B7': (90, 490), 'C7': (170, 490), 'D7': (250, 490), 'E7': (330, 490), 'F7': (410, 490), 'G7': (490, 490), 'H7': (570, 490),
    'A8': (10, 570), 'B8': (90, 570), 'C8': (170, 570), 'D8': (250, 570), 'E8': (330, 570), 'F8': (410, 570), 'G8': (490, 570), 'H8': (570, 570),
}


class mainFigure:

    def __init__ (self, pixelPosition_X: str, pixelPosition_Y: str, imageObjectPath, figureOnBoard: bool = False, figureChanged: bool = False): 

        pixelPosition_X = str(pixelPosition_X)
        pixelPosition_Y = str(pixelPosition_Y)

        self.literally_position = (pixelPosition_X) + pixelPosition_Y

        self.pixelPosition_X = mainFigure.__currentCellsCoordinates((pixelPosition_X + pixelPosition_Y))[0]
        self.pixelPosition_Y = mainFigure.__currentCellsCoordinates((pixelPosition_X + pixelPosition_Y))[1]
        
        self.imageObjectPath = imageObjectPath

        self.figureOnBoard = figureOnBoard
        self.figureChanged = figureChanged

        self.rect = pygame.Rect(self.pixelPosition_X, self.pixelPosition_Y, 80, 80)

        self.imageObject = pygame.transform.scale(pygame.image.load(imageObjectPath).convert_alpha(), (80, 80))
        


    def draw(self, surface: pygame.Surface) -> pygame.Surface:

        surface.blit(self.imageObject, self.rect)


    def __currentCellsCoordinates(numCell):
        return ((Cells_coordinate[numCell][0] + 40), (Cells_coordinate[numCell][1] + 40))


    def updatePosition(self, pos_x, pos_y) -> pygame.Rect:

        self.pixelPosition_X = pos_x
        self.pixelPosition_Y = pos_y

        self.rect = pygame.Rect(self.pixelPosition_X, self.pixelPosition_Y, 80, 80)


    def take_position(self):
        print(self.literally_position)

