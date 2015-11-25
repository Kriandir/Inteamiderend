import visual

#dit is een dictionary die ik heb aangemaakt die de laatste tile toegevoegd opslaat
#en removed met behulp van remove

class locationDic:
    # hier geinitilatiseerd voor ons probleem
    def __init__(self):
        self.last = None
        self.dict = {7:[],5:[],3:[],2:[]}
    # hier gooit ie dus de tegel in de dict en defineert laatst toegevoegde tegel
    def add(self,tile,coords):
        self.last = tile
        self.dict[tile].append(coords)
    #het enige probleem is dat het hele systeem werkt enkel met 1 tegel
    #als ik twee keer pop gaat het fout
    # wss moet ik dus nog een extra clas maken

    def remove(self):
        coordinate = []
        coordinate = self.dict[self.last].pop()
        return coordinate

    def peek(self):
        return self.dict


# dit is de stack waarmee ik werk dus

class Stack:
    #inilatiseerd de dictionary en de items

    def __init__(self):
        self.items = []
        self.locationdic = locationDic()
        self.grid = [[0]*17 for n in range(17)]

    def push(self,tile):
        apple = self.placetile(tile)
        if apple:
            self.items.append(tile)

    def placetile(self,tile):
        groundZero = False
    #Finding a zero in the grid where the tile wouldn't go outside the board.
        y = 0
        for row in self.grid:
            x = 0
            for gridValue in row:
                if gridValue == 0 and x+tile <= 17 and y+tile <= 17:
                    groundZero = True

    #Breaks loop when there is a non-zero, else fills in tile.
                    for i in range(y, y+tile):
                        for j in range(x, x+tile):
                            if self.grid[i][j] > 0:
                                groundZero = False
                                break
                        if not groundZero:
                            break
                    else:

                        for i in range(y, y+tile):
                            for j in range(x, x+tile):
                                self.grid[i][j] += 1
                        self.show()

                        self.location(x,y,tile)
                        return True


                x += 1
            y += 1

        if not groundZero:
            print "woops"
            return False

    def location(self,x,y,tile):
        coordinate= [x,y]
        self.locationdic.add(tile,coordinate)

    def pop(self):
        coordinate = self.locationdic.remove()
        tile = self.items.pop()
        x = coordinate[0]
        y = coordinate[1]
        for i in range(y, y+tile):
            for j in range(x, x+tile):
                self.grid[i][j] = 0


    def show(self):
        visualization = visual.visualizationGrid(17, 17, 20, self.grid)
        visualization.drawGrid()


    def peek(self):
        return self.items
    def peeklib(self):
        return self.locationdic.peek()


s = Stack()
s.push(7)
s.push(7)
s.push(7)
print s.peeklib()
s.pop()
print s.peeklib()
s.show()
