import pygame

class visualizationGrid:
    def __init__(self, widthBoard, heightBoard, sizeTile, grid):
        self.widthBoard = widthBoard
        self.heightBoard = heightBoard
        self.sizeTile = sizeTile
        self.grid = grid


        # Initializing screen.
        widthScreen = self.sizeTile*self.widthBoard
        heightScreen = self.sizeTile*self.heightBoard
        self.screen = pygame.display.set_mode((widthScreen, heightScreen))

        # Initializing colors.
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue =(0,0,255)
        self.purple = (255,0,255)

    def drawGrid(self):
        y = 0
        for row in self.grid:
            x = 0
            for col in row:

                if col == 0:
                    pygame.draw.rect(self.screen, self.black, (x, y, self.sizeTile, self.sizeTile))
                if col >= 1:
                    pygame.draw.rect(self.screen, self.white, (x, y, self.sizeTile, self.sizeTile))

                if col % 2 == 1:
                    pygame.draw.rect(self.screen, self.red, (x, y, self.sizeTile, self.sizeTile))

                if col % 3 == 1:
                    pygame.draw.rect(self.screen, self.blue, (x, y, self.sizeTile, self.sizeTile))

                if col % 4 == 1:
                    pygame.draw.rect(self.screen, self.purple, (x, y, self.sizeTile, self.sizeTile))






                pygame.draw.rect(self.screen, self.green, (x, y, self.sizeTile, self.sizeTile), 1)
                x += self.sizeTile

            y += self.sizeTile

        pygame.display.update()
