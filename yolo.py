import visual

# Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

grid = [[0]*widthBoard for n in range(heightBoard)]
tiles = sorted([2,3,3,3,3,3,3,3,5,5,5,7,7,7], reverse=True)
colorTile = 0

colorTile = 1

for tile in tiles:
    # Vind een 0 in de grid.
    groundZero = False
    y = 0
    for row in grid:
        x = 0
        for gridValue in row:
            if gridValue == 0: # 0 gevonden

                # Controleren of de tegel niet buiten het bord zou vallen.
                if x+tile > widthBoard or y+tile > heightBoard:

                    break
                if y+tile > heightBoard:
                    y = 0
                    break


                groundZero = True
                # Check of in het bereik van de tegel alleen maar nullen staan.
                for i in range(y, y+tile):
                    for j in range(x, x+tile):
                        if grid[i][j] != 0:
                            groundZero = False
                            break
                    if groundZero == False:
                        break

            if groundZero == True:
                break
            x += 1
        if groundZero == True:
            break


        y += 1


    # Tegel invullen op de coordinaten.
    if groundZero == True:
        for i in range(y, y+tile):
            for j in range(x, x+tile):

                grid[i][j] += colorTile


    colorTile +=1

# Visualization.
#while(True):
visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, grid)
visualization.drawGrid()
