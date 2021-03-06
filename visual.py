import pygame

class visGrid:
    def __init__(self, widthBoard, heightBoard, sizeTile, grid):
        #Sizes board.
        self.widthBoard = widthBoard
        self.heightBoard = heightBoard
        self.sizeTile = sizeTile
        
        self.grid = grid

        #Initializing screen.
        widthScreen = self.sizeTile*self.widthBoard
        heightScreen = self.sizeTile*self.heightBoard
        self.screen = pygame.display.set_mode((widthScreen, heightScreen))

        #Initializing colors.
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.green = (0,200,0)
        self.blue =(100,180,255)
        self.pink = (255,0,200)
        self.yellow = (255,255,0)
        self.purple = (150,0,255)
        self.grey = (192,192,192)
        self.orange = (255,150,0)
        self.turquoise = (0,255,180)
        
        self.colors = [self.green,self.red,self.turquoise,self.blue,self.pink,self.yellow,self.purple,self.grey,self.orange]

    def drawGrid(self):
        numberOfColors = len(self.colors)
        y = 0
        for row in self.grid:
            x = 0
            for col in row:
                col2 = col-int(col/numberOfColors)*numberOfColors
                for i in range(numberOfColors):
                    if col2 == i:
                        pygame.draw.rect(self.screen, self.colors[i],(x, y, self.sizeTile, self.sizeTile))
                if col == 0:
                    pygame.draw.rect(self.screen, self.black, (x, y, self.sizeTile, self.sizeTile))

                #Rooster maken.
                pygame.draw.rect(self.screen, self.black, (x, y, self.sizeTile, self.sizeTile), 1)
                
                x += self.sizeTile
            y += self.sizeTile

        pygame.display.update()
