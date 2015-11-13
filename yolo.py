import visual

# Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

grid = [[0]*widthBoard for n in range(heightBoard)]
tiles = [2,3,3,3,3,3,3,3,5,5,5,7,7,7]

tile = max(tiles)

# Loop over elke tegel.
####

# Coördinaten vinden waar de tegel past.

#Vind een 0 in de grid.
for y in grid:
    for x in y:
        if x == 0:
            goedeplek = True # een 0 gevonden
            # Check of
            for i in range(y, y+tile):
                for j in range(x, x+tile):
                    if j != 0:
                        goedeplek = False
                        break
                if goedeplek == False:
                    break
        if goedeplek == True:
            break
    if goedeplek == True:
        break
                
print x,y


# Tegel invullen op de coördinaten.
for i in range(y, y+tile):
    for j in range(x, x+tile):
        grid[i][j] += 1

# Gebruikte tegel uit lijst verwijderen.
tiles.remove(tile)




# Visualization.
visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, grid)
visualization.drawGrid()
