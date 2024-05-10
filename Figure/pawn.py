import pygame
from Figure.mainClass import mainFigure

# Инициализация Pygame
pygame.init()


class pawnFigure(mainFigure):
    def __init__(self, pixelPosition_X: str, pixelPosition_Y: str, imageObjectPath, player: str, figureOnBoard: bool =True):
        super().__init__(pixelPosition_X, pixelPosition_Y, imageObjectPath, player, figureOnBoard)

        self.starting_position_maintained = True


    def __calculate_moves(self, cell_position, index):
        moves_list = []

        if self.starting_position_maintained:
            moves_list.extend(mainFigure._reposition_cell(position=cell_position, change_number=index * (i+1)) for i in range(2))
        else:
            moves_list.append(mainFigure._reposition_cell(position=cell_position, change_number=index * 1))

        return moves_list


    def __calculate_attack_moves(self, cell_position, index):
        moves_list = []

        for change_letter in [-1, 1]:
            move = mainFigure._reposition_cell(position=cell_position, change_number= index * 1, change_letter= change_letter)
            if move is not None:
                moves_list.append(move)

        return moves_list


    def rule(self, white_list: list = None, black_list: list = None, cell_start = None, cell_end = None, cell_list: list = None):
        moves_list = []

        used_list = self._determine_which_list(white=white_list, black=black_list)

        cell_position = cell_start.colPosition + cell_start.rowPosition

        side_index = -1 if used_list == black_list else 1


        try:

            if cell_end.figureOn is None:
                moves_list = self.__calculate_moves(cell_position, side_index)
            else:
                moves_list = self.__calculate_attack_moves(cell_position, side_index)

            return (cell_end.colPosition + cell_end.rowPosition) in moves_list

        except Exception as e:
            print(f"Error --> pawn.rule - : {e}")
            return False


