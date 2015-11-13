import visual1

grid = [[0]*17 for n in range(17)]

tiles = [2,3,3,3,3,3,3,3,5,5,5,7,7,7]

tile =  max(tiles)


for i in range(tile):
    for j in range(tile):
        grid[i][j] += 1

print grid


anim = visual1.visualizationgameboard(17,17,20,grid)
anim.draw()
