import pygame,sys
from pygame.locals import*
from sys import exit

pygame.init()

# Size Board
widthBoard = 23
heightBoard = 27

# Maten Scherm
widthScreen = 20*widthBoard
heightScreen = 20*heightBoard

grid = [[0]*widthBoard for n in range(heightBoard)]
grid[4][0] = 1
print grid

widthTile = widthScreen/widthBoard
heightTile = heightScreen/heightBoard

black = (0,0,0)
white = (255,255,255)
screen = pygame.display.set_mode((widthScreen, heightScreen))


def draw():
    x,y = 0,0
    for row in grid:
        for col in row:
            if col == 0:
                pygame.draw.rect(screen, black, (x, y, widthTile, heightTile))
            else:
                pygame.draw.rect(screen, white, (x, y, widthTile, heightTile))
            pygame.draw.rect(screen, white, (x, y, widthTile, heightTile), 1)

            x += widthTile
        y += heightTile
        x = 0


while True:
    draw()
    pygame.display.update()
