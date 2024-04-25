import sys
import pygame

from cell import Cell

from Figure.queen import queenFigure
from Figure.king import kingFigure
from Figure.bishop import bishopFigure
from Figure.knight import knightFigure
from Figure.pawn import pawnFigure
from Figure.rook import rookFigure


pygame.init()

LISTOFNUMBER = ("1", "2", "3", "4", "5", "6", "7", "8")
LISTOFLETTERS = ("A", "B", "C", "D", "E", "F", "G", "H")

_BLACKLIST, _WHITELIST, _FULL_LIST = [], [], []


class Board(object):

    def __init__(self, screen: pygame.surface.Surface, player: str):

        self.screen = screen

        self.player = player

        self.size_object = 80

        self.cells = self.__create_cells_board()
        self.figure = self.__create_figure_board()

        self.changed_figure = None


    def __create_cells_board(self) -> list:

        _BOARD_SIZE = 8
        _START_X = 50
        _START_Y = 50
        
        COLORS = [True, False]

        listOfCells = []

        for row in range(_BOARD_SIZE):
            for column in range(_BOARD_SIZE):  

                cellColor = COLORS[(row + column) % 2]  
                
                # Create cell object
                cell = Cell(
                    cellColor=cellColor,
                    pixelPosition_X=_START_X + column * self.size_object,  
                    pixelPosition_Y=_START_Y + row * self.size_object,  
                    rowPosition=LISTOFNUMBER[row],
                    colPosition=LISTOFLETTERS[column],
                )

                listOfCells.append(cell)

        return listOfCells
    

    def __create_figure_board(self):
        def create_piece(piece_class, color, row, col):
            piece_name = 'N' if piece_class == knightFigure else piece_class.__name__[0]
            image_path = f"Figure/Image/{color[0].lower()}{piece_name.lower()}.svg"
            return piece_class(pixelPosition_X=LISTOFLETTERS[col], pixelPosition_Y=row, imageObjectPath=image_path)  # Reverse the row number

        if self.player == 'WHITE':
            king_row, queen_row, pawn_row, opponent_king_row, opponent_pawn_row = 1, 1, 2, 8, 7  # Reverse the row numbers
        else:
            king_row, queen_row, pawn_row, opponent_king_row, opponent_pawn_row = 8, 8, 7, 1, 2  # Reverse the row numbers

        kingW = create_piece(kingFigure, 'w', king_row, 4)
        queenW = create_piece(queenFigure, 'w', queen_row, 3)
        bishopsW = [create_piece(bishopFigure, 'w', king_row, col) for col in (2, 5)]
        knightsW = [create_piece(knightFigure, 'w', king_row, col) for col in (1, 6)]
        rooksW = [create_piece(rookFigure, 'w', king_row, col) for col in (0, 7)]
        pawnsW = [create_piece(pawnFigure, 'w', pawn_row, col) for col in range(8)]

        kingB = create_piece(kingFigure, 'b', opponent_king_row, 4)
        queenB = create_piece(queenFigure, 'b', opponent_king_row, 3)
        bishopsB = [create_piece(bishopFigure, 'b', opponent_king_row, col) for col in (2, 5)]
        knightsB = [create_piece(knightFigure, 'b', opponent_king_row, col) for col in (1, 6)]
        rooksB = [create_piece(rookFigure, 'b', opponent_king_row, col) for col in (0, 7)]
        pawnsB = [create_piece(pawnFigure, 'b', opponent_pawn_row, col) for col in range(8)]

        _WHITELIST = [kingW, queenW] + bishopsW + knightsW + rooksW + pawnsW
        _BLACKLIST = [kingB, queenB] + bishopsB + knightsB + rooksB + pawnsB
        _FULL_LIST = _WHITELIST + _BLACKLIST

        return _FULL_LIST, _WHITELIST, _BLACKLIST





    def draw_board(self):
        for cell in self.cells: cell.draw(self.screen)


    def __setFiguresCellsActive(listOfFigures: list, listOfCells: list = None):
        for figure in listOfFigures:
            for cell in listOfCells:

                if figure.rect.colliderect(cell.rect):
                    cell.active = True


    def click_connection(self) -> tuple:

        mouse_position = pygame.mouse.get_pos()

        try:
            for cell in self.cells:
                if cell.rect.collidepoint(mouse_position):

                    for figure in self.figure[0]:
                        if figure.rect.collidepoint(mouse_position):

                            self.changed_figure = figure
                            
                            return cell, figure
                        
                    return cell, None
        
        except Exception as e:
            print(f"An exception occurred: {e}")

        return None, None
    

    def move_figure(self):

        _now_cell_figure = self.click_connection()

        if _now_cell_figure[1] == None:
            if self.changed_figure != None:

                self.changed_figure.updatePosition((_now_cell_figure[0]).pixelPosition_X, (_now_cell_figure[0]).pixelPosition_Y)
                self.changed_figure.take_position()
                self.changed_figure = None


    def drawLineOfBoard(self) -> pygame.draw:

        pygame.draw.line(self.screen, (0, 56, 34), (48, 48), (48, 690), 2)  # Левая граница
        pygame.draw.line(self.screen, (0, 56, 34), (690, 48), (690, 690), 2)  # Правая граница
        
        pygame.draw.line(self.screen, (0, 56, 34), (50, 48), (690, 48), 2)  # Верх граница
        pygame.draw.line(self.screen, (0, 56, 34), (50, 690), (690, 690), 2)  # Нижняя граница



