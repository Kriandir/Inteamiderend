import visual
import copy
#import cProfile

#Niet meer outcommenten -> functie?


#Sizes Board
#widthBoard = 17
#heightBoard = 17
widthBoard = 23
heightBoard = 27
#widthBoard = 55
#heightBoard = 56
sizeTile = 20

emptyGrid = [[0]*widthBoard for n in range(heightBoard)]
#tilesX = tiles = [7,7,7,5,5,5,3,3,3,3,3,3,3,2]
#tilesY = tiles = [7,7,7,5,5,5,3,3,3,3,3,3,3,2]
tilesX = [10,9,9,8,8,7,7,6,5,4,4,3,3,2,1]
tilesY = [10,9,8,8,8,7,6,6,5,10,4,6,3,2,1]
#tilesX = [20,19,19,18,16,16,14,14,12,12,10,9,9,7,7,6,5,4,2,1]
#tilesY = [21,20,18,17,17,15,15,13,13,11,11,10,8,8,6,5,4,3,3,2]
colorTile = 0

#Places the tile on the first possible position in the grid. Else returns False.
def tilePlacer(grid,x,y,tileX,tileY,colorTile):
    groundZero = True
    if x+tileX <= widthBoard and y+tileY <= heightBoard:
        for i in range(y, y+tileY):
            for j in range(x, x+tileX):
                if grid[i][j] > 0:
                    groundZero = False
                    break
            if not groundZero:
                break
        else:
            for i in range(y, y+tileY):
                for j in range(x, x+tileX):
                    grid[i][j] = colorTile
            return grid

    return False

#Receives a grid and a list with tiles which are not placed yet, and returns a list with all possible children (where one more tile is placed).
def generateAllChildren(parent,tilesX,tilesY,colorTile):
    children = []
    colorTile += 1
    copyTilesX1 = copy.deepcopy(tilesX)
    copyTilesY1 = copy.deepcopy(tilesY)
    y = 0
    for row in parent:
        x = 0
        for gridValue in row:
            if gridValue == 0:
                for i in range(len(copyTilesX1)):
                    copyParent = copy.deepcopy(parent)
                    tileX = tilesX[i]
                    tileY = tilesY[i]
                    gridWithPlacedTile = tilePlacer(copyParent,x,y,tileX,tileY,colorTile)
                    if gridWithPlacedTile:
                        copyTilesX2 = copy.deepcopy(tilesX)
                        copyTilesY2 = copy.deepcopy(tilesY)
                        del copyTilesX2[i]
                        del copyTilesY2[i]
                        children.append([gridWithPlacedTile,copyTilesX2,copyTilesY2,colorTile])
                break #return children

            x += 1
        if gridValue == 0:
            break
        y += 1
        
    return children


def searchForSolution(parent,tilesX,tilesY,colorTile):
    if tilesX:
        children = generateAllChildren(parent,tilesX,tilesY,colorTile)
        for child in children:
            visualization = visual.visualizationGrid(widthBoard,heightBoard,sizeTile,child[0])
            visualization.drawGrid()
            solution = searchForSolution(child[0],child[1],child[2],child[3])
            if solution:
                return solution
        else:
            return False
    return parent

solution = searchForSolution(emptyGrid,tilesX,tilesY,colorTile)

visualization = visual.visualizationGrid(widthBoard,heightBoard,sizeTile,solution)
visualization.drawGrid()
#solution = cProfile.run('searchForSolution(emptyGrid,tiles,colorTile)')
