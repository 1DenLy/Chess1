import pygame
from Figure.mainClass import mainFigure

# Инициализация Pygame
pygame.init()


class kingFigure(mainFigure):
    def __init__(self, pixelPosition_X: str, pixelPosition_Y: str, imageObjectPath, figureOnBoard: bool =True, figureSelected: bool =False):
        super().__init__(pixelPosition_X, pixelPosition_Y, imageObjectPath, figureOnBoard, figureSelected)




















