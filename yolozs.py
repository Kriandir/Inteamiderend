import visual1

grid = [[0]*17 for n in range(17)]

tiles = [2,3,3,3,3]
tilez = [[0*2 for n in range(2)]]

# tile =  max(tiles)




def placingtiles(tile,i,j,ctr):
        if grid[i][j] != 0:
            if j < 17:
                j += 1
                if j > 16:
                    j = 0
                    i+=1

            #     #     return placingtiles(tile,i,j)
            #     # else:
            #     #     return placingtiles(tile,i,j)
            # if i < 17:
            #     i += 1
            #     if i > 16:
            #         i = 0
            #     #     return placingtiles(tile,i,j)
            #     # else:
            #     #     return placingtiles(tile,i,j)
            ctr = 0
            return placingtiles(tile,i,j,ctr)

        if ctr == (tile*tile):
            print ctr

            return True


        else:

            ctr +=1;
        
            grid[i][j] +=1
            return placingtiles(tile,i,j,ctr)



for tile in tiles:
    # for i in range(tile):
    #     for j in range(tile):
    placingtiles(tile,0,0,0)

# for i in range(tile):
#     for j in range(tile):
#         grid[i][j] += 1

print grid

while True:
    anim = visual1.visualizationgameboard(17,17,20,grid)
    anim.draw()
