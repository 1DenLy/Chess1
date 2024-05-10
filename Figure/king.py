import pygame
from Figure.mainClass import mainFigure

# Инициализация Pygame
pygame.init()


class kingFigure(mainFigure):
    def __init__(self, pixelPosition_X: str, pixelPosition_Y: str, imageObjectPath, player: str, figureOnBoard: bool =True):
        super().__init__(pixelPosition_X, pixelPosition_Y, imageObjectPath, player, figureOnBoard)

        self.starting_position_maintained = True


    def rule(self, white_list: list = None, black_list: list = None, cell_start = None, cell_end = None, cell_list: list = None):


        def __checking_the_presence_figure_in_position(position: str, list: list) -> bool:
            return any((cell.colPosition + cell.rowPosition) == position and cell.figureOn is not None for cell in list)


        def __check_route_king(start_position, end_position):
            route = []

            start_column, start_row = start_position[0], int(start_position[1])
            end_column, end_row = end_position[0], int(end_position[1])

            # Check if it's a valid move for the king (1 step in any direction)
            if abs(ord(start_column) - ord(end_column)) <= 1 and abs(start_row - end_row) <= 1:
                
                if __checking_the_presence_figure_in_position(end_position, cell_list):

                    if (cell_start.figureOn in white_list and cell_end.figureOn in black_list) or (
                        cell_start.figureOn in black_list and cell_end.figureOn in white_list
                    ):
                        route.append(end_position)
                else:
                    route.append(end_position)

            return route

        # Create movement route list
        route_figure = __check_route_king( start_position= (cell_start.colPosition + cell_start.rowPosition), 
                                            end_position= (cell_end.colPosition + cell_end.rowPosition) )

        return (cell_end.colPosition + cell_end.rowPosition) in route_figure


