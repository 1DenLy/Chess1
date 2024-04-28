import pygame
from Figure.mainClass import mainFigure

# Инициализация Pygame
pygame.init()


class bishopFigure(mainFigure):
    def __init__(self, pixelPosition_X: str, pixelPosition_Y: str, imageObjectPath, player: str, figureOnBoard: bool =True, figureSelected: bool =False):
        super().__init__(pixelPosition_X, pixelPosition_Y, imageObjectPath, player, figureOnBoard, figureSelected)

    def rule(self, players_move: str, list_cell: list, white_list: list, black_list: list):


        return True

