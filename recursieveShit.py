import visual

#Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

grid = [[0]*widthBoard for n in range(heightBoard)]
tiles = sorted([2,3,3,3,3,3,3,3,5,5,5,7,7,7], reverse=True)
colorTile = 1

class Board():
    def __init__(self, grid, colorTile):
        self.grid = grid
        self.colorTile = colorTile
    def tilePlacer(self, tile):
        groundZero = False
        y = 0
        for row in self.grid:
            x = 0
            for gridValue in row:
                if gridValue == 0:
                    groundZero = True
                    if x+tile <= widthBoard and y+tile <= heightBoard:
                        for i in range(y, y+tile):
                            for j in range(x, x+tile):
                                if self.grid[i][j] > 0:
                                    groundZero = False
                                    break
                            if not groundZero:
                                break
                        else:
                            for i in range(y, y+tile):
                                for j in range(x, x+tile):
                                    self.grid[i][j] += colorTile
                            return self.grid
                   
                x += 1
            y += 1
            
        else:
            return False


def generateAllChildren(parent,tiles,colorTile):
    children = []
    for tile in tiles: #moet eigenlijk versch. waarden zijn
        placedTile = Board(parent,colorTile).tilePlacer(tile)
        if placedTile:
            colorTile += 1
            children.append([placedTile,tiles])
    return children

def vulVolgendeTegelIn(parent,tiles,colorTile):
    children = generateAllChildren(parent,tiles,colorTile)
    for child in children:
        if child[1] == []:
            print 'bingo'
            break
        else:
            vulVolgendeTegelIn(child,tiles,colorTile)

vulVolgendeTegelIn(grid,tiles,colorTile)


#Open visualization.
while(True):
    visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, grid)
    visualization.drawGrid()
