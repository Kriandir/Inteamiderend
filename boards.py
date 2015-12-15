def boards(board):

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

# One board from Daan.
    elif board == 11:
        widthBoard = 24
        heightBoard = 78
        tiles = [[9,12],[9,3],[18,16],[10,17],[20,4],[5,4],[16,19],[13,9],\
                 [19,10],[5,20],[2,10],[10,11],[16,8],[15,14]]
        sizeTile = 7
    elif board == 12:
        widthBoard = 26
        heightBoard = 72
        tiles = [[9,12],[9,3],[18,16],[10,17],[20,4],[5,4],[16,19],[13,9],\
                 [19,10],[5,20],[2,10],[10,11],[16,8],[15,14]]
        sizeTile = 7
    elif board == 13:
        widthBoard = 36
        heightBoard = 52
        tiles = [[9,12],[9,3],[18,16],[10,17],[20,4],[5,4],[16,19],[13,9],\
                 [19,10],[5,20],[2,10],[10,11],[16,8],[15,14]]
        sizeTile = 7
    elif board == 14:
        widthBoard = 39
        heightBoard = 48
        tiles = [[9,12],[9,3],[18,16],[10,17],[20,4],[5,4],[16,19],[13,9],\
                 [19,10],[5,20],[2,10],[10,11],[16,8],[15,14]]
        sizeTile = 7


    return [widthBoard,heightBoard,tiles,sizeTile]
