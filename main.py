import pygame
from checkers.constants import WIDTH, HEIGHT

FPS = 60

# Tworzenie okna gry
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Warcaby')


def main():
    run = True
    # ustawienie odswiezania na 60FPS dzieki czemu bedziemy mieli plynna rozgrywke
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit()


main()
