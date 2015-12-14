import visual
import copy
import itertools
import cProfile

#profiler -> waar zit tijd in?
#hoeveel oplossingen zijn er?
#tegels draaien
#state space
#hoeveel iteraties
#kleuren verbeteren
#kernwoord: volgorde tiles
#meer comments en niet meer dan 80 tekens achter elkaar

def solveBoard(board,showVisual):
#Initializing boards.
    if board == 1:
        widthBoard = 17
        heightBoard = 17
        tiles = [[7,7],[7,7],[7,7],[5,5],[5,5],[5,5],[3,3],[3,3],[3,3],[3,3],\
                 [3,3],[3,3],[3,3],[2,2]]
        sizeTile = 20
    elif board == 2:
        widthBoard = 23
        heightBoard = 27
        tiles = [[10,10],[9,9],[9,8],[8,8],[8,8],[7,7],[7,6],[6,6],[5,5],\
                 [4,10],[4,4],[3,6],[3,3],[2,2],[1,1]]
        sizeTile = 20
    elif board == 3:
        widthBoard = 55
        heightBoard = 56
        tiles = [[20,21],[19,20],[19,18],[18,17],[16,17],[16,15],[14,15],\
                 [14,13],[12,13],[12,11],[10,11],[9,10],[9,8],[7,8],[7,6],\
                 [6,5],[5,4],[4,3],[2,3],[1,2]]
        sizeTile = 10
    elif board == 4:
        widthBoard = 12
        heightBoard = 17
        tiles = [[5,5],[6,4],[6,4],[5,4],[5,3],[5,3],[7,2],[6,2],[6,2],[5,2],\
                 [4,2],[3,2],[5,1],[5,1],[4,1],[3,1],[2,1]]
        sizeTile = 20
    elif board == 5:
        widthBoard = 19
        heightBoard = 20
        tiles = [[6,6],[6,6],[6,6],[6,6],[6,5],[6,4],[6,4],[5,4],[6,3],[6,3],\
                 [6,3],[5,3],[6,2],[6,2],[4,3],[3,3],[6,1],[6,1],[3,2],[3,2]]
        sizeTile = 20
    elif board == 6:
        widthBoard = 37
        heightBoard = 22
        tiles = [[13,7],[8,7],[11,5],[10,5],[7,6],[7,6],[13,3],[12,3],[7,5],\
                 [7,5],[6,5],[6,5],[6,5],[7,4],[6,4],[6,4],[7,3],[7,3],[5,4],\
                 [6,3],[5,3],[5,3],[5,3],[7,2],[5,2],[4,2],[2,2],[3,1],[3,1]]
        sizeTile = 15
                
    emptyGrid = [[0]*widthBoard for n in range(heightBoard)]
    colorTile = 0

#If it fits, places the tile on the given position in the grid. Else returns False.
    def tilePlacer(grid,x,y,tileX,tileY,colorTile):
        if x+tileX <= widthBoard and y+tileY <= heightBoard:
            for i in range(y, y+tileY):
                for j in range(x, x+tileX):
                    if grid[i][j] > 0:
                        return False
                    else:
                        grid[i][j] = colorTile
            return grid

#Receives a grid and a list of tiles, and returns a list with all possible children (where one more tile is placed).
    def generateAllChildren(parent,tiles,colorTile):
        children = []
        colorTile += 1
        uniqueTiles = list(tiles for tiles,_ in itertools.groupby(tiles)) #To avoid duplicate children.
        y = 0
        for row in parent:
            x = 0
            for gridValue in row:
                if gridValue == 0:
                    for tile in uniqueTiles:
                        copyParent = copy.deepcopy(parent)
                        tileX = tile[0]
                        tileY = tile[1]
                        gridWithPlacedTile = tilePlacer(copyParent,x,y,tileX,tileY,colorTile)
                        if gridWithPlacedTile:
                            copyTiles = list(tiles)
                            copyTiles.remove(tile)
                            children.append([gridWithPlacedTile,copyTiles,colorTile])
                    return children

                x += 1
            y += 1
            
        return [] #Only happens if the board is already full, but there are still tiles left, then there are no children.

#Checks whole board to see if there are smaller spaces in x direction than the smallest tile.
    def checkBoard(grid,tiles):
        lowX = min(tiles)[0]
        
        for row in grid:
            x = 0
            chain = 0
            for gridValue in row:
                if gridValue == 0:
                    chain += 1
                    if x == widthBoard-1:
                        if chain < lowX:
                            return False
                if gridValue > 0:
                    if lowX > chain > 0:
                        return False
                    chain = 0
                x += 1

        return True 

#Recursive function for depth-first search for the solution of the board.
    def searchForSolution(parent,tiles,colorTile):
        if tiles:
            if not checkBoard(parent,tiles):
                return False
            children = generateAllChildren(parent,tiles,colorTile)
            for child in children:
                if showVisual:
                    visual.visualizationGrid(widthBoard,heightBoard,sizeTile,child[0]).drawGrid()
                solution = searchForSolution(child[0],child[1],child[2])
                if solution:
                    return solution
            else:
                return False
        return parent

    solution = searchForSolution(emptyGrid,tiles,colorTile)
    
    if solution:
        print 'yolo'
        #while(True):
        #    visual.visualizationGrid(widthBoard,heightBoard,sizeTile,solution).drawGrid()
    else:
        print 'This board has no solution!'
cProfile.run('solveBoard(1,False)')
#cProfile.run('re.compile("solveBoard(2,False)")')
