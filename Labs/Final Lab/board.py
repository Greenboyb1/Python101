class Board:
    def __init__(self, width, height):
        """
        The board is stored as a dictionary of tuples and booleans.

        """
        self.width = width
        self.height = height

        self.board = {}
        for x in range(width):
            for y in range(height):
                self.board[(x, y)] = False
        print("done")

    def get(self, x, y):
        return self.board[(x, y)]

    def set(self, x, y, value):
        self.board[(x, y)] = value

    def switch(self, x, y):
        if self.board[(x, y)]:
            self.board[(x, y)] = False
        else:
            self.board[(x, y)] = True

    def liveOrDie(self, x, y):
        # Returns true if the cell should be alive next iteration. Otherwise, returns false.
        #if there are 3 alive sq around the sq, it is alive, if more that 3 dead, if less that 2 dead, if 2 and square was              alive then stays alive, but if it was dead, stay dead

        # Number of living squares boardering the target square
        livingSquares = 0

        xLess = x - 1
        xMore = x + 1

        yLess = y - 1
        yMore = y + 1

        if x == 0:
            xLess = self.width-1
        elif x == self.width-1:
            xMore = 0

        if y == 0:
            yLess = self.height - 1
        elif y == self.height-1:
            yMore = 0

        # if x+1 != xMore:
        #     print("x+1 is not xmore")
        # if x-1 != xLess:
        #     print("x-1 is not xless")
        # if y+1 != yMore:
        #     print("y+1 is not ymore")
        # if y-1 != yLess:
        #     print("y-1 is not yless")
        # print("hi")

        xCheck = (xLess, x, xMore)
        yCheck = (yLess, y, yMore)

        for i in xCheck:
            for j in yCheck:
                if not(i == x and j == y):
                    if self.board[(i, j)]:
                        livingSquares += 1

        if livingSquares <= 1:
            return False
        elif livingSquares >= 4:
            return False
        elif not self.board[(x, y)] and livingSquares == 2:
            return False
        else:
            return True


    def next(self):
        nextBoard = {}
        for x in range(self.width):
            for y in range(self.height):
                nextBoard[(x, y)] = self.liveOrDie(x, y)
        self.board = nextBoard
        # advances the board to the next generation
