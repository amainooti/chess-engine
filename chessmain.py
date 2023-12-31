"""
    This is the main driver file, it's responsible for handling user input and displaying current
    game state object.
"""

import pygame as p
from chessengine import Gamestate, Move

# variables declarations
p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8 # dimension of the chess board 8x8
SQ_SIZE = HEIGHT // DIMENSION #square size of the chess board
MAX_FPS = 15
IMAGES = {}

'''
    loading into memory is an expensive operation, so we only want to load it once and not
    every frame


    initialize a global variable of images which will be called exactly once in the main
'''

def loadImages():
    pieces = ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR", "wp", "bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "bp"]
    for piece in pieces:
        image = p.image.load(f"images/{piece}.png")
        IMAGES[piece] = p.transform.scale(image, (SQ_SIZE, SQ_SIZE))

    # NOTE YOU CAN ACCESS AN IMAGE BY IMAGES['wp']


"""
the main driver for our code, this will handle user input and updating the graphics
"""

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = Gamestate()
    loadImages()  # only do this once
    running = True
    sqSelected = ()
    playerClicks = []  # keeps track of the player clicks, this is a tuple: [(6, 4)]
    print(playerClicks)
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                x, y = p.mouse.get_pos()
                col = x // SQ_SIZE
                row = y // SQ_SIZE
                if sqSelected == (row, col):  # undo selection
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                    print(playerClicks)
                if len(playerClicks) == 2:
                    move = Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.get_chess_notations())
                    gs.makeMove(move)
                    sqSelected = ()
                    playerClicks = []

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for all the graphics within a current game state
'''


def drawBoard(screen):
    colors = p.Color("white"), p.Color("dark green")
    # draw pieces on the board using the current GameState.board
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))



def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #not an empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawGameState(screen, gs):
    drawBoard(screen) # draw squares on the board
    drawPieces(screen, gs.board) # draw

if __name__ == "__main__":
    main()