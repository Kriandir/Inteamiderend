import visual

# Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

grid = [[0]*widthBoard for n in range(heightBoard)]
tiles = sorted([2,3,3,3,3,3,3,3,5,5,5,7,7,7], reverse=False)

for tile in tiles:

    # Vind een 0 in de grid.
    groundZero = False
    for row in grid:
        y = grid.index(row)
        for x in row:
            if x == 0: # 0 gevonden
                
                # Controleren of de tegel niet buiten het bord zou vallen.
                if y+tile >= heightBoard or x+tile >= widthBoard:
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
        if groundZero == True:
            break
        
    # Tegel invullen op de coördinaten.
    if groundZero == True:
        for i in range(y, y+tile):
            for j in range(x, x+tile):
                grid[i][j] += 1


    # Gebruikte tegel uit lijst verwijderen.
    tiles.remove(tile)


# Visualization.
visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, grid)
visualization.drawGrid()
