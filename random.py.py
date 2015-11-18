import visual
import random

#Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

grid = [[0]*widthBoard for n in range(heightBoard)]
tiles = sorted([2,3,3,3,3,3,3,3,5,5,5,7,7,7], reverse=True)

placedTiles = []
placedCounter = 0
colorTile = 1

def tilePlacer(tile, colorTile, randomTileNumber):
#Finding a zero in the grid where the tile wouldn't go outside the board.
    groundZero = False
    for row in grid:
        y = grid.index(row)
        for gridValue in row:
            x = row.index(gridValue)
            if gridValue == 0 and x+tile <= widthBoard and y+tile <= heightBoard:
                groundZero = True
                
#Breaks loop when there is a non-zero, else fills in tile.
                for i in range(y, y+tile):
                    for j in range(x, x+tile):
                        if grid[i][j] > 0:
                            groundZero = False
                            break
                    if groundZero == False:
                        break
                else:
                    for i in range(y, y+tile):
                        for j in range(x, x+tile):
                            grid[i][j] += colorTile
                    return [x,y]
                
    if not groundZero:
        return False


henkie = {2:[],3:[],5:[],7:[]}
for i in range(1000):
    randomTileNumber = random.randint(0,len(tiles)-1)
    tile = tiles[randomTileNumber]
    coordPlacedTile = tilePlacer(tile, colorTile, randomTileNumber)
    if coordPlacedTile:
        henkie[tile].append(coordPlacedTile)
        colorTile += 1
        placedTiles.append(tiles[randomTileNumber])
        placedCounter += 1
        tiles.remove(tiles[randomTileNumber])
        print henkie
        print tiles
    #if not coordPlacedTile:
     #   print placedTiles[-1]
            
#Open visualization.
while(True):
    visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, grid)
    visualization.drawGrid()
