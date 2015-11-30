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
        self.pink = (255,0,255)
        self.yellow = (255,255,0)
<<<<<<< HEAD
        self.orange = (200,100,0)
        self.purple = (150,0,255)
        
        self.colors = [self.white, self.red, self.blue, self.pink, self.yellow,self.orange, self.purple]
        self.numberOfColors = len(self.colors)
        
=======
        self.orange = (255,100,0)
        self.purple = (150,0,255)
        self.colorlist = [self.black, self.white, self.red, self.blue, self.pink, self.yellow,self.orange, self.purple]
>>>>>>> 7c90535aaf090f64a6b2cd7db0b67aa3767210f2
    def drawGrid(self):
        y = 0
        for row in self.grid:
            x = 0
            for col in row:
<<<<<<< HEAD
                col = col-int(col/self.numberOfColors)*self.numberOfColors
                for i in range(self.numberOfColors):
                    if col == i:
                        pygame.draw.rect(self.screen, self.colors[i],(x, y, self.sizeTile, self.sizeTile))
=======
                for i in range(1,len(self.colorlist)):
                    if col % i == 0:
                        pygame.draw.rect(self.screen,self.colorlist[i],(x,y, self.sizeTile,self.sizeTile))
                if col == 0:
                    pygame.draw.rect(self.screen, self.black, (x, y, self.sizeTile, self.sizeTile))
>>>>>>> 7c90535aaf090f64a6b2cd7db0b67aa3767210f2
                pygame.draw.rect(self.screen, self.green, (x, y, self.sizeTile, self.sizeTile), 1)
                x += self.sizeTile
            y += self.sizeTile

        pygame.display.update()
