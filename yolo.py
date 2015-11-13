import visual1

# Sizes Board
widthBoard = 17
heightBoard = 17
sizeTile = 20

grid = [[0]*widthBoard for n in range(heightBoard)]

tiles = [2,3,3,3,3,3,3,3,5,5,5,7,7,7]

tile =  max(tiles)

for i in range(tile):
    for j in range(tile):
        grid[i][j] += 1

print grid




#anim = visual1.visualizationgameboard(widthBoard, heightBoard, sizeTile, grid)
#anim.draw()
