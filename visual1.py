import pygame

class visualizationgameboard:
    def __init__(self,widthBoard,heightBoard,sizeTile):
        self.widthBoard = widthBoard
        self.heightBoard = heightBoard
        self.sizeTile = sizeTile
        # Sizes Screen
        self.widthScreen = sizeTile*widthBoard
        self.heightScreen = sizeTile*heightBoard

        self.grid = [[0]*widthBoard for n in range(heightBoard)]
        ##grid[4][0] = 1
        #print grid

        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.screen = pygame.display.set_mode((self.widthScreen, self.heightScreen))

    def draw(self):
        x,y = 0,0
        for row in self.grid:
            for col in row:

                if col == 0:
                    pygame.draw.rect(self.screen, self.black, (x, y, self.sizeTile, self.sizeTile))
                elif col == 1:
                    pygame.draw.rect(self.screen, self.white, (x, y, self.sizeTile, self.sizeTile))
                else:
                    pygame.draw.rect(self.screen, self.red, (x, y, self.sizeTile, self.sizeTile))

                pygame.draw.rect(self.screen, self.white, (x, y, self.sizeTile, self.sizeTile), 1)
                x += self.sizeTile

            y += self.sizeTile
            x = 0
anim = visualizationgameboard(17,17,20)
anim.draw()
pygame.display.update()
