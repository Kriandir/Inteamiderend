import visual

#Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

grid = [[0]*widthBoard for n in range(heightBoard)]
tiles = sorted([2,3,3,3,3,3,3,3,5,5,5,7,7,7], reverse=True)
colorTile = 1

groundZero = False
y = 0
for row in grid:
    x = 0
    for gridValue in row:
        if gridValue == 0:
            for tile in tiles:
                groundZero = True
                if x+tile <= widthBoard and y+tile <= heightBoard:
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
                        tiles.remove(tile)
                        colorTile += 1
                        break
           
        x += 1
    y += 1

#Open visualization.
while(True):
    visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, grid)
    visualization.drawGrid()
