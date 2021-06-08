import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, BLACK, WHITE_TURN, BLACK_TURN, WINNER_WHITE, WINNER_BLACK, WHITE, BLACK
from checkers.game import Game
from checkers.winnerDisplay import WinnerDisplay
import time

FPS = 60

# Tworzenie okna gry
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Warcaby')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    # ustawienie odswiezania na 60FPS dzieki czemu bedziemy mieli plynna rozgrywke
    clock = pygame.time.Clock()

    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            winner = game.winner()
            if(winner == WHITE):
                winnerDisplay = WinnerDisplay(WINNER_WHITE, WIN)
                winnerDisplay.draw()
            else:
                winnerDisplay = WinnerDisplay(WINNER_BLACK, WIN)
                winnerDisplay.draw()
            pygame.display.update()
            time.sleep(2)

            game.reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if(row >= 8):
                    if(col == 7):
                        game.reset()
                else:
                    game.select(row, col)

        game.update()
    pygame.quit()


main()
