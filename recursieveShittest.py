import visual

#Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

grid = [[0]*widthBoard for n in range(heightBoard)]
tiles = sorted([2,3,3,3,3,3,3,3,5,5,5,7,7,7], reverse=True)
tiles = [2,3]
colorTile = 1

def tilePlacer(grid,tile,colorTile):
    groundZero = False
    y = 0
    for row in grid:
        x = 0
        for gridValue in row:
            if gridValue == 0:
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
                        return grid
            x += 1
        y += 1
        
    else:
        return False
    

def generateAllChildren(parent,tiles,colorTile):
    children = []
    copyTiles = list(tiles)
    for tile in tiles: #moet eigenlijk versch. waarden zijn -> set
        gridWithPlacedTile = tilePlacer(parent,tile,colorTile)
        if gridWithPlacedTile:
            copyTiles.remove(tile)
            colorTile += 1
            children.append([gridWithPlacedTile,copyTiles,colorTile])
    return children

def vulVolgendeTegelIn(parent,tiles,colorTile):
    if tiles:
        children = generateAllChildren(parent,tiles,colorTile)
        print children
        for child in children:
            vulVolgendeTegelIn(child[0],child[1],child[2])
    return parent

grid = vulVolgendeTegelIn(grid,tiles,colorTile)


#Open visualization.
while(True):
    visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, grid)
    visualization.drawGrid()
