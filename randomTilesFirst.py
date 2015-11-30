import random
import visual

#Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

grid = [[0]*widthBoard for n in range(heightBoard)]
startTiles = [2,3,3,3,3,3,3,3,5,5,5,7,7,7]
colorTile = 1
trials = 10

def tilePlacer(tile, colorTile):
    groundZero = False
#Finding a zero in the grid where the tile wouldn't go outside the board.
    y = 0
    for row in grid:
        x = 0
        for gridValue in row:
            if gridValue == 0 and x+tile <= widthBoard and y+tile <= heightBoard:
                groundZero = True
#Breaks loop when there is a non-zero, else fills in tile.
                for i in range(y, y+tile):
                    for j in range(x, x+tile):
                        if grid[i][j] > 0:
                            groundZero = False
                            break
                    if not groundZero:
                        break
                else:
                    for i in range(y, y+tile):
                        for j in range(x, x+tile):
                            grid[i][j] += colorTile
                    return True
            x += 1
        y += 1
        
    if not groundZero:
        return False


counterCounter = 0
for i in range(trials):
    counter = 0
    tiles = list(startTiles)
    
    while tiles:
        counter += 1
        grid = [[0]*widthBoard for n in range(heightBoard)]
        tiles = list(startTiles)

        while tiles:
            randomTileNumber = random.randint(0,len(tiles)-1)
            tile = tiles[randomTileNumber]
            if tilePlacer(tile, colorTile):
                del tiles[randomTileNumber]
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
