import visual

#Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

grid = [[0]*widthBoard for n in range(heightBoard)]
tiles = sorted([2,3,3,3,3,3,3,3,5,5,5,7,7,7], reverse=True)

colorTile = 1
for tile in tiles:
    
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
                    colorTile +=1
                    break
                    
        if groundZero:
            break
        
#Open visualization.
while(True):
    visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, grid)
    visualization.drawGrid()
