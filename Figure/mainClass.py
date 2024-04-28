import pygame

# Инициализация Pygame
pygame.init()

def create_cells_coordinates(color):

    if color not in ['WHITE', 'BLACK']:

        raise ValueError("Invalid color. Use 'White' or 'Black'.")
        
    if color == 'WHITE':
        letters = 'ABCDEFGH'
        numbers = '87654321'
    elif color == 'BLACK':
        letters = 'HGFEDCBA'
        numbers = '12345678'

    cells_coordinate = {}

    for j, number in enumerate(numbers):
        for i, letter in enumerate(letters):
        
            cells_coordinate[letter + number] = (10 + i*80, 10 + j*80)
    
    return cells_coordinate



class mainFigure:

    def __init__ (self, pixelPosition_X: str, pixelPosition_Y: str, imageObjectPath, player: str, figureOnBoard: bool = False, figureChanged: bool = False): 

        pixelPosition_X = str( pixelPosition_X )
        pixelPosition_Y = str( pixelPosition_Y )

        self.literally_position = pixelPosition_X + pixelPosition_Y

        self.pixelPosition_X = mainFigure.__currentCellsCoordinates(  numCell= ( pixelPosition_X + pixelPosition_Y ), dict_coordinate= ( create_cells_coordinates(player) )  )[0]
        self.pixelPosition_Y = mainFigure.__currentCellsCoordinates(  numCell= ( pixelPosition_X + pixelPosition_Y ), dict_coordinate= ( create_cells_coordinates(player) )  )[1]
        
        self.imageObjectPath = imageObjectPath

        self.figureOnBoard = figureOnBoard
        self.figureChanged = figureChanged

        self.rect = pygame.Rect( self.pixelPosition_X, self.pixelPosition_Y, 80, 80 )

        self.imageObject = pygame.transform.scale( pygame.image.load( imageObjectPath ).convert_alpha(), (80, 80) )
        


    def draw(self, surface: pygame.Surface) -> pygame.Surface:

        surface.blit(self.imageObject, self.rect)


    def __currentCellsCoordinates(dict_coordinate, numCell):
        return ( (dict_coordinate[numCell][0] + 40), (dict_coordinate[numCell][1] + 40) )


    def updatePosition(self, pos_x, pos_y) -> pygame.Rect:
        
        self.pixelPosition_X = pos_x
        self.pixelPosition_Y = pos_y

        self.rect = pygame.Rect( self.pixelPosition_X, self.pixelPosition_Y, 80, 80 )


