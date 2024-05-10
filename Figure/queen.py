import pygame
from Figure.mainClass import mainFigure

# Инициализация Pygame
pygame.init()


class queenFigure(mainFigure):
    def __init__(self, pixelPosition_X: str, pixelPosition_Y: str, imageObjectPath, player: str, figureOnBoard: bool =True):
        super().__init__(pixelPosition_X, pixelPosition_Y, imageObjectPath, player, figureOnBoard)


    def rule(self, white_list: list = None, black_list: list = None, cell_start = None, cell_end = None, cell_list: list = None):

        def __checking_the_presence_figure_in_position(position: str, list: list) -> bool:
            return any((cell.colPosition + cell.rowPosition) == position and cell.figureOn is not None for cell in list)


        def __is_valid_rook_move(start_position, end_position):
            start_col, start_row = ord(start_position[0].upper()) - ord('A'), int(start_position[1]) - 1
            end_col, end_row = ord(end_position[0].upper()) - ord('A'), int(end_position[1]) - 1
            return start_col == end_col or start_row == end_row


        def __check_route_queen(start_position, end_position):
            route = []

            start_column, start_row = start_position[0], int(start_position[1])
            end_column, end_row = end_position[0], int(end_position[1])

            # Check if it's a horizontal, vertical, or diagonal move
            if start_column == end_column or start_row == end_row or abs(ord(start_column) - ord(end_column)) == abs(start_row - end_row):
                col_step = 0 if start_column == end_column else 1 if ord(start_column) < ord(end_column) else -1
                row_step = 0 if start_row == end_row else 1 if start_row < end_row else -1

                col, row = ord(start_column) + col_step, start_row + row_step
                while col != ord(end_column) + col_step or row != end_row + row_step:
                    if __checking_the_presence_figure_in_position(chr(col) + str(row), cell_list):
                        if chr(col) + str(row) == cell_end.colPosition + cell_end.rowPosition:
                            if (cell_start.figureOn in white_list and cell_end.figureOn in black_list) or (
                                cell_start.figureOn in black_list and cell_end.figureOn in white_list
                            ):
                                route.append(chr(col) + str(row))
                                break
                            else:
                                break
                        else:
                            break
                    else:
                        route.append(chr(col) + str(row))
                        col += col_step
                        row += row_step

            return route
        
        route_figure = __check_route_queen( start_position= (cell_start.colPosition + cell_start.rowPosition), end_position= (cell_end.colPosition + cell_end.rowPosition) )

        return (cell_end.colPosition + cell_end.rowPosition) in route_figure

