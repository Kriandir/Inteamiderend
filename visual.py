import pygame

# Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

# Sizes Screen
widthScreen = sizeTile*widthBoard
heightScreen = sizeTile*heightBoard

grid = [[0]*widthBoard for n in range(heightBoard)]
grid[4][0] = 1
print grid

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
screen = pygame.display.set_mode((widthScreen, heightScreen))

def draw():
    x,y = 0,0
    for row in grid:
        for col in row:
            if col == 0:
                pygame.draw.rect(screen, black, (x, y, sizeTile, sizeTile))
            else if(col == 1):
                pygame.draw.rect(screen, white, (x, y, sizeTile, sizeTile))
            else:
                pygame.draw.rect(screen, red, (x, y, sizeTile, sizeTile))
            pygame.draw.rect(screen, white, (x, y, sizeTile, sizeTile), 1)
            x += sizeTile
        y += sizeTile
        x = 0
        
while(True):
    draw()
    pygame.display.update()
