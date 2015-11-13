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

# Co�rdinaten vinden waar de tegel past.

#Vind een 0 in de grid.
x,y = 0,-1
for row in grid:
    y += 1
    for x in row:
        if x == 0:
            goedeplek = True # een 0 gevonden
            
            # Check of in het bereik van de tegel alleen maar 0en staan.
            for i in range(y, y+tile):
                for j in range(x, x+tile):
                    if grid[i][j] != 0:
                        goedeplek = False
                        
        if goedeplek == True:
            break
    if goedeplek == True:
        break


# Tegel invullen op de co�rdinaten.
for i in range(y, y+tile):
    for j in range(x, x+tile):
        grid[i][j] += 1

# Gebruikte tegel uit lijst verwijderen.
tiles.remove(tile)


# Visualization.
visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, grid)
visualization.drawGrid()
