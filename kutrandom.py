import random
import visual

#Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

grid = [[0]*widthBoard for n in range(heightBoard)]
tiles = [2,3,3,3,3,3,3,3,5,5,5,7,7,7]

placedTilesDict = {2:[],3:[],5:[],7:[]}
placedTiles = []
colorTile = 1
trials = 5

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
                    return True #return [x,y]
                
            x += 1
        y += 1
        
    if not groundZero:
        return False
    
countercounter = 0
for i in range(trials):
    counter = 0
    tiles = [2,3,3,3,3,3,3,3,5,5,5,7,7,7]
    
    while tiles != []:
        counter += 1
        grid = [[0]*widthBoard for n in range(heightBoard)]
        tiles = [2,3,3,3,3,3,3,3,5,5,5,7,7,7]

        for i in range(100):
            if len(tiles)>0:
                randomTileNumber = random.randint(0,len(tiles)-1)
                tile = tiles[randomTileNumber]
                #coordPlacedTile = tilePlacer(tile, colorTile)
                #if coordPlacedTile:
                if tilePlacer(tile, colorTile):
                    #placedTilesDict[tile].append(coordPlacedTile)
                    #placedTiles.append(tile)
                    tiles.remove(tiles[randomTileNumber])
                    colorTile += 1
                    #x = placedTilesDict.get(placedTiles[-1])[-1][0]
            else:
                break
    print counter
    countercounter += counter

print 'Gemiddeld:',countercounter/trials


#Open visualization.
while(True):
    visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, grid)
    visualization.drawGrid()
