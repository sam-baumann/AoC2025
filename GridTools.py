class GridTools:
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

    def __init__(self, fname=None, gridLines=None, grid=None):
        """
        supply fname, gridLines, or grid, if multiple are supplied, precedence goes 1. grid 2. fname 3. gridLines
        """
        if fname is None and gridLines is None and grid is None:
            raise Exception("supply fname, gridLines, or grid")
        if fname is not None:
            with open(fname) as file:
                gridLines = file.readlines()
        if grid is not None:
            self.grid = grid
        elif gridLines is not None:
            self.grid = [list(x.strip()) for x in gridLines]

    def rows(self):
        """
        this refers to the 'x' dimension
        """
        return len(self.grid)

    def cols(self):
        """
        this refers to the 'y' dimension
        """
        return len(self.grid[0])

    def isInBounds(self, x, y):
        if x >= self.rows() or x < 0 or y >= self.cols() or y < 0:
            return False
        return True

    def gridAtVector(self, vec):
        x = vec[0]
        y = vec[1]
        if self.isInBounds(x, y):
            return self.grid[x][y]
        return None

    def gridAtOffset(self, x, y, offset):
        offX, offY = offset
        x += offX
        y += offY
        if not self.isInBounds(x, y):
            return None
        else:
            return self.grid[x][y]

    def printGrid(self):
        print(str(self))

    def __repr__(self):
        ret = ""
        ret += "*" * self.cols()
        ret += "\n"
        for row in self.grid:
            ret += "".join([str(x) for x in row])
            ret += "\n"
        ret += "*" * self.cols()
        return ret

    def addVector(self, first, second):
        if len(first) != len(second):
            return None
        return tuple([x + y for x, y in zip(first, second)])
