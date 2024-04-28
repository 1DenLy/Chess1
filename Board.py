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

        self.move = 0

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

        if self.player == "WHITE":
            row_positions = LISTOFNUMBER[::-1]  # Reverse the list for white player
            col_positions = LISTOFLETTERS
        else:
            row_positions = LISTOFNUMBER
            col_positions = LISTOFLETTERS[::-1]  # Reverse the list for black player

        for column in range(_BOARD_SIZE):
            for row in range(_BOARD_SIZE):  
                cellColor = COLORS[(row + column) % 2]  
                
                # Create cell object
                cell = Cell(
                    cellColor=cellColor,
                    pixelPosition_X=_START_X + column * self.size_object,  
                    pixelPosition_Y=_START_Y + row * self.size_object,  
                    rowPosition=row_positions[row],
                    colPosition=col_positions[column],
                )

                listOfCells.append(cell)

        return listOfCells


    def __create_figure_board(self):

        def __create_piece(figures_class, color, row, col):

            piece_name = 'N' if figures_class == knightFigure else figures_class.__name__[0]
            image_path = f"Figure/Image/{color[0].lower()}{piece_name.lower()}.svg"

            return figures_class(
                pixelPosition_X=col_positions[col-1],  
                pixelPosition_Y=row_positions[row-1],  
                imageObjectPath=image_path,
                player=self.player
            )

        row_positions = LISTOFNUMBER
        col_positions = LISTOFLETTERS

        if self.player == 'WHITE':

            king_row, queen_row, pawn_row, opponent_king_row, opponent_pawn_row = 1, 1, 2, 8, 7
            player_color, opponent_color = 'w', 'b'

        else:

            king_row, queen_row, pawn_row, opponent_king_row, opponent_pawn_row = 8, 8, 7, 1, 2
            player_color, opponent_color = 'b', 'w'

        kingP = __create_piece(kingFigure, player_color, king_row, 5)
        queenP = __create_piece(queenFigure, player_color, queen_row, 4)
        bishopsP = [__create_piece(bishopFigure, player_color, king_row, col) for col in (3, 6)]
        knightsP = [__create_piece(knightFigure, player_color, king_row, col) for col in (2, 7)]
        rooksP = [__create_piece(rookFigure, player_color, king_row, col) for col in (1, 8)]
        pawnsP = [__create_piece(pawnFigure, player_color, pawn_row, col) for col in range(1, 9)]

        kingO = __create_piece(kingFigure, opponent_color, opponent_king_row, 5)
        queenO = __create_piece(queenFigure, opponent_color, opponent_king_row, 4)
        bishopsO = [__create_piece(bishopFigure, opponent_color, opponent_king_row, col) for col in (3, 6)]
        knightsO = [__create_piece(knightFigure, opponent_color, opponent_king_row, col) for col in (2, 7)]
        rooksO = [__create_piece(rookFigure, opponent_color, opponent_king_row, col) for col in (1, 8)]
        pawnsO = [__create_piece(pawnFigure, opponent_color, opponent_pawn_row, col) for col in range(1, 9)]


        _WHITELIST  = [kingP, queenP] + bishopsP + knightsP + rooksP + pawnsP
        _BLACKLIST  = [kingO, queenO] + bishopsO + knightsO + rooksO + pawnsO

        _FULL_LIST  = _WHITELIST + _BLACKLIST

        return _FULL_LIST, _WHITELIST, _BLACKLIST


    def draw_board(self):
        for cell in self.cells: cell.draw(self.screen)


    def drawLineOfBoard(self) -> pygame.draw:

        pygame.draw.line(self.screen, (0, 56, 34), (48, 48), (48, 690), 2)  # Левая граница
        pygame.draw.line(self.screen, (0, 56, 34), (690, 48), (690, 690), 2)  # Правая граница
        
        pygame.draw.line(self.screen, (0, 56, 34), (50, 48), (690, 48), 2)  # Верх граница
        pygame.draw.line(self.screen, (0, 56, 34), (50, 690), (690, 690), 2)  # Нижняя граница


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
                            
                            return cell, figure
                        
                    return cell, None
        
        except Exception as e:
            print(f"An exception occurred: {e}")

        return None, None
    

    def move_figure(self):

        def move(cell):
            
            self.changed_figure.updatePosition(cell.pixelPosition_X, cell.pixelPosition_Y)
            self.changed_figure = None
            self.move += 1

        def get_figure(figure_now_clicked, figure_changed, cell_now):

            self.figure[0].remove(figure_now_clicked)

            if figure_now_clicked in self.figure[1]: self.figure[1].remove(figure_now_clicked)
            elif figure_now_clicked in self.figure[2]: self.figure[2].remove(figure_now_clicked)

            figure_changed.updatePosition(cell_now.pixelPosition_X, cell_now.pixelPosition_Y)
            self.changed_figure = None
            self.move += 1


        last_click_cell, last_click_figure = self.click_connection() # <-- Click results in variable


        # Click ---> Cell and Figure 
        if last_click_cell != None and last_click_figure != None: 

            # Check changed_figure
            if ( self.changed_figure != None ):

                if ( (self.move % 2 == 0) and (self.changed_figure in self.figure[1]) ) or ( (self.move % 2 != 0) and (self.changed_figure in self.figure[2]) ):

                    if self.changed_figure.rule(list_cell= self.cells, white_list= self.figure[1], black_list=self.figure[2], players_move=self.move) == True:

                        get_figure(figure_now_clicked=last_click_figure, figure_changed=self.changed_figure, cell_now=last_click_cell)

                else: 
                    self.changed_figure = last_click_figure

            else: 
                if ( ( self.move % 2 == 0 and last_click_figure in self.figure[1] ) or ( self.move % 2 != 0 and last_click_figure in self.figure[2])):

                    self.changed_figure = last_click_figure 

        else:

            # Click ---> Cell and None
            if last_click_cell != None and last_click_figure == None: 

                if self.changed_figure != None:

                    if self.changed_figure.rule(list_cell= self.cells, white_list= self.figure[1], black_list=self.figure[2], players_move=self.move) == True:

                        move(last_click_cell)

                    else: self.changed_figure = None

        
        print(self.move)
        print('Changed figure -', self.changed_figure)



