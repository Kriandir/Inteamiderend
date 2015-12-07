import visual
import copy

def solveBoard(board,vis):
    if board == 1:
        widthBoard = 17
        heightBoard = 17
        tiles = [[7,7],[7,7],[7,7],[5,5],[5,5],[5,5],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[2,2]]
        #tilesY = [7,7,7,5,5,5,3,3,3,3,3,3,3,2]
        sizeTile = 20
    elif board == 2:
        widthBoard = 23
        heightBoard = 27
        tilesX = [10,9,9,8,8,7,7,6,5,4,4,3,3,2,1]
        tilesY = [10,9,8,8,8,7,6,6,5,10,4,6,3,2,1]
        sizeTile = 20
    elif board == 3:
        widthBoard = 55
        heightBoard = 56
        tilesX = [20,19,19,18,16,16,14,14,12,12,10,9,9,7,7,6,5,4,2,1]
        tilesY = [21,20,18,17,17,15,15,13,13,11,11,10,8,8,6,5,4,3,3,2]
        sizeTile = 8

    emptyGrid = [[0]*widthBoard for n in range(heightBoard)]
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
        y = 0
        for row in parent:
            x = 0
            for gridValue in row:
                if gridValue == 0:
                    for i in range(len(tilesX)):
                        copyParent = copy.deepcopy(parent)
                        tileX = tilesX[i]
                        tileY = tilesY[i]
                        gridWithPlacedTile = tilePlacer(copyParent,x,y,tileX,tileY,colorTile)
                        if gridWithPlacedTile:
                            copyTilesX = copy.deepcopy(tilesX)
                            copyTilesY = copy.deepcopy(tilesY)
                            del copyTilesX[i]
                            del copyTilesY[i]
                            children.append([gridWithPlacedTile,copyTilesX,copyTilesY,colorTile])
                    return children

                x += 1
            y += 1


    def searchForSolution(parent,tilesX,tilesY,colorTile):
        if tilesX:
            children = generateAllChildren(parent,tilesX,tilesY,colorTile)
            for child in children:
                if vis:
                    visual.visualizationGrid(widthBoard,heightBoard,sizeTile,child[0]).drawGrid()
                solution = searchForSolution(child[0],child[1],child[2],child[3])
                if solution:
                    return solution
            else:
                return False
        return parent

    solution = searchForSolution(emptyGrid,tilesX,tilesY,colorTile)
    visual.visualizationGrid(widthBoard,heightBoard,sizeTile,solution).drawGrid()
    
solveBoard(1,True)
