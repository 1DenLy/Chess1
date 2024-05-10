import pygame
from Figure.mainClass import mainFigure

# Инициализация Pygame
pygame.init()


class knightFigure(mainFigure):
    def __init__(self, pixelPosition_X: str, pixelPosition_Y: str, imageObjectPath, player: str, figureOnBoard: bool =True):
        super().__init__(pixelPosition_X, pixelPosition_Y, imageObjectPath, player, figureOnBoard)

    def rule(self, white_list: list = None, black_list: list = None, cell_start = None, cell_end = None, cell_list: list = None):
        moves_list = []

        cell_position = cell_start.colPosition + cell_start.rowPosition
        changes = [(1, -2), (2, -1), (-1, -2), (-2, -1), (1, 2), (2, 1), (-1, 2), (-2, 1)]

        for change_number, change_letter in changes:
            move = mainFigure._reposition_cell(position=cell_position, change_number=change_number, change_letter=change_letter)
            if move is not None:
                moves_list.append(move)

        return cell_end.colPosition + cell_end.rowPosition in moves_list
