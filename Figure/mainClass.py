import pygame
import sys, os

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

    def __init__ (self, pixelPosition_X: str, pixelPosition_Y: str, image_objectPath, player: str, figureOnBoard: bool = False): 

        pixelPosition_X = str( pixelPosition_X )
        pixelPosition_Y = str( pixelPosition_Y )

        self.literally_position = pixelPosition_X + pixelPosition_Y

        self.pixelPosition_X = mainFigure.__currentCellsCoordinates(  num_cell= ( pixelPosition_X + pixelPosition_Y ), dict_coordinate= ( create_cells_coordinates(player) )  )[0]
        self.pixelPosition_Y = mainFigure.__currentCellsCoordinates(  num_cell= ( pixelPosition_X + pixelPosition_Y ), dict_coordinate= ( create_cells_coordinates(player) )  )[1]

        self.image_objectPath = mainFigure.__resource_path(image_objectPath)

        self.figureOnBoard = figureOnBoard

        self.rect = pygame.Rect( self.pixelPosition_X, self.pixelPosition_Y, 80, 80 )

        self.image_object = pygame.transform.scale( pygame.image.load( image_objectPath ).convert_alpha(), (80, 80) )


    def __resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


    def draw(self, surface: pygame.Surface) -> pygame.Surface:

        surface.blit(self.image_object, self.rect)


    def __currentCellsCoordinates(dict_coordinate, num_cell):
        return ( (dict_coordinate[num_cell][0] + 40), (dict_coordinate[num_cell][1] + 40) )


    def updatePosition(self, x_diagonal_position, y_diagonal_position) -> pygame.Rect:
        
        self.pixelPosition_X = x_diagonal_position
        self.pixelPosition_Y = y_diagonal_position

        self.rect = pygame.Rect( self.pixelPosition_X, self.pixelPosition_Y, 80, 80 )


    def _determine_which_list(self, white, black) -> list:

        if self in white: used_list = white

        elif self in black: used_list = black

        return used_list


    def _reposition_cell(position: str, change_letter: int = 0, change_number: int = 0) -> str:

        if len(position) == 2:
            letter = position[0]
            number = position[1]

        try:

            if change_letter != 0:

                new_letter = chr(ord(letter) + change_letter)

                if 'A' <= new_letter <= 'H':
                    letter = new_letter
                else:
                    return None


            if change_number != 0:

                new_number = int(number) + change_number
                
                if 1 <= new_number <= 8:
                    number = str(new_number)
                else:
                    return None
                
        except Exception as ex:
            print(f"Error in `mainFigure --> reposition_cell` {ex}")

        return (letter + number)