import pygame
from .constants import GREEN, WHITE, WIDTH, HEIGHT, SMALLFONT


class ResetBtn:
    def __init__(self, win):
        self.color = GREEN
        self.f_color = WHITE
        self.width = WIDTH//8
        self.height = HEIGHT//8
        self.text = SMALLFONT.render('RESET', True, self.f_color)
        self.win = win
        self.draw()

    def draw(self):
        pygame.draw.rect(self.win, self.color, (WIDTH -
                         self.width, HEIGHT - self.height, WIDTH, HEIGHT))
        self.win.blit(self.text, (WIDTH-75, HEIGHT-60))
