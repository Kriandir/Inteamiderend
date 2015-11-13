import visual

grid = [[0]*17 for n in range(17)]

tiles = [2,3,3,3,3,3,3,3,5,5,5,7,7,7]

formaat =  max(tiles)

for i in range(formaat):
    for j in range(formaat):
        grid[i][j] += 1

print grid
visualizationgameboard.draw(grid)
#while(True):
 #   draw()
  #  pygame.display.update()
