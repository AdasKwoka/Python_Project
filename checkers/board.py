import pygame
from .constants import GRAY, SQUARE_SIZE, COLS, ROWS, BLACK, WHITE, BLACK
from .piece import Piece


class Board:
    def __init__(self):
        # przechowywanie obiektow w dwuwymiarowej tablicy
        self.board = []
        self.red_left = self.green_left = 12
        self.white_kings = self.black_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(GRAY)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE,
                                 col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        # Nie zmiennia pionkow na poczatkowych pozycjach poniewaz musza sie poruszyc
        if row == ROWS or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.black_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
