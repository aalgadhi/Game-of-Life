class Cell:
    startingPoint = 0, 0
    cellSize = 40
    def __init__(self, i, j, alive = False):
        self.i = i
        self.j = j
        self.y = Cell.translate(Cell.startingPoint[0], i, Cell.cellSize)
        self.x = Cell.translate(Cell.startingPoint[1], j, Cell.cellSize)
        self.alive = alive
        self.nextAlive = alive
    
    def neighbors(self, grid):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (self.i + i < 0 or self.i + i >= len(grid) or self.j + j < 0 or self.j + j >= len(grid[0]) or i == 0 and j == 0):
                    continue
                else:
                    neighbors.append([self.i + i, self.j + j])
        return neighbors
    
    def die(self, grid):
        _neighbors = self.neighbors(grid)
        aliveCells = 0
        for neighbor in _neighbors:
            if grid[neighbor[0]][neighbor[1]].alive == True:
                aliveCells += 1
        if aliveCells >= 2 and aliveCells < 4:
            self.nextAlive = True
        else:
            self.nextAlive = False
        
    def calculateStartingPoint(WIDTH, HEIGHT, horizontalcellsNo, verticalcellsNo, cellSize = 40):
        startingX = (WIDTH - (cellSize + 1) * horizontalcellsNo)/2
        startingY = (HEIGHT - (cellSize + 1) * verticalcellsNo)/2
        return startingY, startingX
    
    def translate(startingPoint, index, sqaureSize):
        return startingPoint + index * (sqaureSize+1)
