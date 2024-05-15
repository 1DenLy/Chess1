import pygame
from Figure.mainClass import mainFigure

# Инициализация Pygame
pygame.init()


class rookFigure(mainFigure):
    def __init__(self, pixelPosition_X: str, pixelPosition_Y: str, imageObjectPath, player: str, figureOnBoard: bool =True):
        super().__init__(pixelPosition_X, pixelPosition_Y, imageObjectPath, player, figureOnBoard)

        self.starting_position_maintained = True

    def rule(self, white_list: list = None, black_list: list = None, cell_start = None, cell_end = None, cell_list: list = None):

        def __checking_the_presence_figure_in_position(position: str, list: list) -> bool:
            return any((cell.colPosition + cell.rowPosition) == position and cell.figureOn is not None for cell in list)


        def __is_valid_rook_move(start_position, end_position):
            start_col, start_row = ord(start_position[0].upper()) - ord('A'), int(start_position[1]) - 1
            end_col, end_row = ord(end_position[0].upper()) - ord('A'), int(end_position[1]) - 1
            return start_col == end_col or start_row == end_row


        def __check_route(start_position, end_position):
            route = []

            start_column, start_row = start_position[0], int(start_position[1])
            end_column, end_row = end_position[0], int(end_position[1])

            # Проверка на совпадение столбцов (букв)
            if start_column == end_column:
                step = 1 if start_row < end_row else -1  # Определение шага движения вверх или вниз

                for row in range(start_row + step, end_row + step, step):

                    if __checking_the_presence_figure_in_position( (start_column + str(row)), cell_list):

                        if (start_column + str(row)) == (cell_end.colPosition + cell_end.rowPosition):
                            if ( (cell_start.figureOn in white_list) and (cell_end.figureOn in black_list) ) or ( (cell_start.figureOn in black_list) and (cell_end.figureOn in white_list) ):
                                route.append( (start_column + str(row)) )
                                break
                            else:
                                break    
                        else:
                            break
                    else:
                        route.append( (start_column + str(row)) )


            # Проверка на совпадение строк (цифр)
            elif start_row == end_row:
                step = 1 if ord(start_column) < ord(end_column) else -1  # Определение шага движения вправо или влево

                for col in range(ord(start_column) + step, ord(end_column) + step, step):

                    if __checking_the_presence_figure_in_position( (chr(col) + str(start_row)), cell_list):
                        
                        if (chr(col) + str(start_row)) == (cell_end.colPosition + cell_end.rowPosition):
                            if ( (cell_start.figureOn in white_list) and (cell_end.figureOn in black_list) ) or ( (cell_start.figureOn in black_list) and (cell_end.figureOn in white_list) ):
                                route.append( (chr(col) + str(start_row)) )
                                break
                            else:
                                break    
                        else:
                            break
                        
                    else:
                        route.append( (chr(col) + str(start_row)) )

            return route


        # Check move is True 
        if not __is_valid_rook_move( start_position= (cell_start.colPosition + cell_start.rowPosition), end_position= (cell_end.colPosition + cell_end.rowPosition) ):
            return False
        
        # Create movement route list
        route_figure = __check_route( start_position= (cell_start.colPosition + cell_start.rowPosition), end_position= (cell_end.colPosition + cell_end.rowPosition) )

        return (cell_end.colPosition + cell_end.rowPosition) in route_figure








