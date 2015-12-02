import visual
import copy
import sys
#import cProfile

#Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

emptyGrid = [[0]*widthBoard for n in range(heightBoard)]
tiles = [7,7,7,5,5,5,3,3,3,3,3,3,3,2]
colorTile = 0

#Places the tile on the first possible position in the grid. Else returns False.
def tilePlacer(grid,tile,colorTile,x,y):
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
                    grid[i][j] = colorTile
            return grid

    return False

#Receives a grid and a list with tiles which are not placed yet, and returns a list with all possible children (where one more tile is placed).
def generateAllChildren(parent,tiles,colorTile):
    children = []
    colorTile += 1
    copyTiles1 = sorted(list(set(copy.deepcopy(tiles))),reverse=True) #So that identical tiles only are used once.
    y = 0
    for row in parent:
        x = 0
        for gridValue in row:
            if gridValue == 0:
                for tile in copyTiles1:
                    copyParent = copy.deepcopy(parent)
                    gridWithPlacedTile = tilePlacer(copyParent,tile,colorTile,x,y)
                    if gridWithPlacedTile:
                        copyTiles2 = copy.deepcopy(tiles)
                        copyTiles2.remove(tile)
                        children.append([gridWithPlacedTile,copyTiles2,colorTile])
                break
            x += 1
            
        if gridValue == 0:
            break
        y += 1
        
    return children


def searchForSolution(parent,tiles,colorTile):
    if tiles:
        children = generateAllChildren(parent,tiles,colorTile)
        if children:
            for child in children:
                visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, child[0])
                visualization.drawGrid()
                searchForSolution(child[0],child[1],child[2])
            else:
                return False
        else:
            return False
    #visualization = visual.visualizationGrid(widthBoard, heightBoard, sizeTile, parent)
    #visualization.drawGrid()
    sys.exit()

searchForSolution(emptyGrid,tiles,colorTile)
#solution = cProfile.run('searchForSolution(emptyGrid,tiles,colorTile)')
