import visual
import itertools
import time
import cProfile

#kleuren verbeteren

# Class to count the total amount of iterations.
class iterationCounter():
    def __init__(self):
        self.counter = 0
    def oneCount(self):
        self.counter += 1
    def giveCounter(self):
        return self.counter

# Class to collect all solutions of the board in a list.
class solvedSolutions():
    def __init__(self):
        self.solutions = []
    def addSolution(self,solution):
        self.solutions.append(solution)
    def giveSolutions(self):
        return self.solutions



def solveBoard(board,showVisual,allSolutions,turning):
# Initializing boards.
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

# Extra boards from the VU.
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
    elif board == 7:
        widthBoard = 31
        heightBoard = 20
        tiles = [[10,6],[8,5],[8,5],[6,6],[6,6],[10,3],[10,3],[6,5],[7,4],\
                 [7,4],[5,5],[8,3],[6,4],[7,3],[5,4],[5,4],[6,3],[6,3],[6,3],\
                 [5,3],[4,3],[3,3],[3,3],[3,2],[5,1],[4,1],[2,2],[2,2],[3,1],\
                 [3,1]]
    elif board == 8:
        widthBoard = 27
        heightBoard = 27
        tiles = [[9,9],[9,9],[9,7],[9,6],[8,6],[7,6],[7,6],[9,4],[9,4],[9,3],\
                 [9,3],[8,3],[5,4],[9,2],[9,2],[6,3],[6,2],[4,3],[9,1],[9,1],\
                 [9,1],[4,2],[6,1],[6,1],[3,2],[5,1],[4,1],[2,2],[2,1],[2,1]]


    emptyGrid = [[0]*widthBoard for n in range(heightBoard)]
    colorTile = 0
    sols = solvedSolutions()
    counter = iterationCounter()


    
# If it fits, places the given tile on the given position in the grid.
# Else returns False.
    def tilePlacer(grid,x,y,tileX,tileY,colorTile):
        if x+tileX <= widthBoard and y+tileY <= heightBoard:
            for i in range(y, y+tileY):
                for j in range(x, x+tileX):
                    if grid[i][j] > 0:
                        return False
                    else:
                        grid[i][j] = colorTile
            return grid



# Receives a grid and a list of tiles that are still left.
    def generateAllChildren(parent,tiles,colorTile):
        children = []
                 
# To avoid duplicate children.
        uniqueTiles = list(tiles for tiles,_ in itertools.groupby(tiles))

# Searches for the first empty space in the grid.
        y = 0
        for row in parent:
            x = 0
            for gridValue in row:
                if gridValue == 0:

# For every tile, makes a new grid with this tile on this space, if possible.
                    for tile in uniqueTiles:
                        copyParent = [list(copyRow) for copyRow in parent]
                        tileX = tile[0]
                        tileY = tile[1]
                        childGrid = tilePlacer(copyParent,x,y,tileX,tileY,\
                                               colorTile)
                        if childGrid:
                            copyTiles = list(tiles)
                            copyTiles.remove(tile)
                            children.append([childGrid,copyTiles])

# If it's a rect, makes another child with the tile turned around, if possible.
                        if turning and tileX != tileY:
                            childGrid = tilePlacer(copyParent,x,y,tileY,tileX,\
                                                   colorTile)
                            if childGrid:
                                copyTiles = list(tiles)
                                copyTiles.remove(tile)
                                children.append([childGrid,copyTiles])
                    return children

                x += 1
            y += 1

        return []



    def checkBoard(grid,tiles):
                 
# Calculates the smallest width or height of the tiles left.
        if turning:
            low = min(min(tile) for tile in tiles)
        else:
            low = min(tiles)[0]

# Returns False if there is a space that is smaller than this. Else True.
        for row in grid:
            x = 0
            sizeSpace = 0
            for gridValue in row:
                if gridValue == 0:
                    sizeSpace += 1
                    if x == widthBoard-1:
                        if sizeSpace < low:
                            return False
                if gridValue > 0:
                    if low > sizeSpace > 0:
                        return False
                    sizeSpace = 0
                x += 1

        return True



# Recursive function for depth-first search for the solutions of the board.
    def searchForSolutions(parent,tiles,colorTile):
        counter.oneCount()
        if tiles:
            colorTile += 1

# If chosen, shows visualization during calculating.
            if showVisual:
                visual.visGrid(widthBoard,heightBoard,sizeTile,\
                               parent).drawGrid()

# Prunes the branch if checkBoard returns False.
            if not checkBoard(parent,tiles):
                return False

# For every child, calls this function again. If the function gives a solution,
# passes it through. At the end of a layer, returns False.
            children = generateAllChildren(parent,tiles,colorTile)
            for child in children:
                gridChild = child[0]
                tilesChild = child[1]
                solution = searchForSolutions(gridChild,tilesChild,colorTile) 
                if solution:
                    return solution     
            else:
                return False

# If a solution is found, adds it to the list or returns it.
        if allSolutions:
            sols.addSolution(parent)
            return False
        else:
            return parent



    solution = searchForSolutions(emptyGrid,tiles,colorTile)
    print 'Total iterations:',counter.giveCounter()
    
    if allSolutions:
        solutions = sols.giveSolutions()   
        print 'Amount of solutions:',len(solutions)

        for sol in solutions:
            visual.visGrid(widthBoard,heightBoard,sizeTile,sol).drawGrid()
            time.sleep(0.5)
            
    elif solution:
        pass
        #while True:
         #   visual.visGrid(widthBoard,heightBoard,sizeTile,solution).drawGrid()

    else:
        print 'This board has no solution!'
            
    

#solveBoard(2,False,False,True)


cProfile.run('solveBoard(3,False,False,True)') 
