import sys
import pygame

pygame.init()

#Constants

Player = 'WHITE'

WIDTH, HEIGHT = 750, 825 
FPS = 60

# Инициализация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Шахматная доска")


from Board import Board

# Main Cycle

Board1 = Board(screen, Player)


clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: # Exit program
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            Board1.move_figure()




    screen.fill((210, 210, 210))  # Clear screen


    Board1.draw_board()

    Board1.drawLineOfBoard()

    for figure in Board1.figure[0]:
        figure.draw(screen)


    pygame.display.flip()
    clock.tick(FPS)

# Завершение программы
pygame.quit()
sys.exit()
