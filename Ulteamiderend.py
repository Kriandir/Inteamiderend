import boards
import visual
import itertools
import time
#import cProfile

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
    chosenBoard = boards.boards(board)
    widthBoard = chosenBoard[0]
    heightBoard = chosenBoard[1]
    tiles = chosenBoard[2]
    sizeTile = chosenBoard[3]
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
        while True:
            visual.visGrid(widthBoard,heightBoard,sizeTile,solution).drawGrid()

    else:
        print 'This board has no solution!'
            
    

solveBoard(4,True,True,True)


#cProfile.run('solveBoard(3,False,False,True)') 
