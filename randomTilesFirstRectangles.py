import random
import visual

#Sizes Board
widthBoard = 23
heightBoard = 27
sizeTile = 20

grid = [[0]*widthBoard for n in range(heightBoard)]
startTilesX = [1,2,3,4,5,6,7,8,8,9,10,9,7,4,3]
startTilesY = [1,2,3,4,5,6,7,8,8,9,10,8,6,10,6]
colorTile = 1
trials = 1

def tilePlacer(tileX, tileY, colorTile):
#Finding a zero in the grid where the tile wouldn't go outside the board.
    y = 0
    for row in grid:
        x = 0
        for gridValue in row:
            if gridValue == 0 and x+tileX <= widthBoard and y+tileY <= heightBoard:
                groundZero = True
#Breaks loop when there is a non-zero, else fills in tile.
                for i in range(y, y+tileY):
                    for j in range(x, x+tileX):
                        if grid[i][j] > 0:
                            groundZero = False
                            break
                    if not groundZero:
                        break
                else:
                    for i in range(y, y+tileY):
                        for j in range(x, x+tileX):
                            grid[i][j] = colorTile
                    return True
            x += 1
        y += 1
        
    return False


counterCounter = 0
for i in range(trials):
    counter = 0
    tilesX = list(startTilesX)
    tilesY = list(startTilesY)
    
    while tilesX:
        counter += 1
        grid = [[0]*widthBoard for n in range(heightBoard)]
        tilesX = list(startTilesX)
        tilesY = list(startTilesY)

        while tilesX:
            randomTileNumber = random.randint(0,len(tilesX)-1)
            tileX = tilesX[randomTileNumber]
            tileY = tilesY[randomTileNumber]
            if tilePlacer(tileX, tileY, colorTile):
                del tilesX[randomTileNumber]
                del tilesY[randomTileNumber]
                colorTile += 1
            else:
                break
    print counter
    counterCounter += counter

print 'Gemiddeld:',counterCounter/trials


#Open visualization.
while(True):
    visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, grid)
    visualization.drawGrid()
