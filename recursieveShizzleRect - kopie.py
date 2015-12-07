import visual
import copy
import itertools

def solveBoard(board,vis):
    if board == 1:
        widthBoard = 17
        heightBoard = 17
        tiles = [[7,7],[7,7],[7,7],[5,5],[5,5],[5,5],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[2,2]]
        sizeTile = 20
    elif board == 2:
        widthBoard = 23
        heightBoard = 27
        tiles = [[10,10],[9,9],[9,8],[8,8],[8,8],[7,7],[7,6],[6,6],[5,5],[4,10],[4,4],[3,6],[3,3],[2,2],[1,1]]
        sizeTile = 20
    elif board == 3:
        widthBoard = 55
        heightBoard = 56
        tiles = [[20,21],[19,20],[19,18],[18,17],[16,17],[16,15],[14,15],[14,13],[12,13],[12,11],[10,11],[9,10],[9,8],[7,8],[7,6],[6,5],[5,4],[4,3],[2,3],[1,2]]
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
    def generateAllChildren(parent,tiles,colorTile):
        children = []
        colorTile += 1
        copyTiles1 = copy.deepcopy(tiles)
        copyTiles1 = list(copyTiles1 for copyTiles1,_ in itertools.groupby(copyTiles1))
        y = 0
        for row in parent:
            x = 0
            for gridValue in row:
                if gridValue == 0:
                    for tile in copyTiles1:
                        copyParent = copy.deepcopy(parent)
                        tileX = tile[0]
                        tileY = tile[1]
                        gridWithPlacedTile = tilePlacer(copyParent,x,y,tileX,tileY,colorTile)
                        if gridWithPlacedTile:
                            copyTiles2 = copy.deepcopy(tiles)
                            copyTiles2.remove(tile)
                            children.append([gridWithPlacedTile,copyTiles2,colorTile])
                    return children

                x += 1
            y += 1


    def searchForSolution(parent,tiles,colorTile):
        if tiles:
            children = generateAllChildren(parent,tiles,colorTile)
            for child in children:
                if vis:
                    visual.visualizationGrid(widthBoard,heightBoard,sizeTile,child[0]).drawGrid()
                solution = searchForSolution(child[0],child[1],child[2])
                if solution:
                    return solution
            else:
                return False
        return parent

    solution = searchForSolution(emptyGrid,tiles,colorTile)
    visual.visualizationGrid(widthBoard,heightBoard,sizeTile,solution).drawGrid()
    
solveBoard(1,True)
