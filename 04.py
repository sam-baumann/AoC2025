from GridTools import GridTools

grid = GridTools("./inputs/04.txt")

def count_adjacent(x, y):
    dirs = [
        grid.addVector(GridTools.UP, GridTools.LEFT), #up-left
        GridTools.UP,
        grid.addVector(GridTools.UP, GridTools.RIGHT), #up-right
        GridTools.RIGHT,
        grid.addVector(GridTools.DOWN, GridTools.RIGHT), #down-right
        GridTools.DOWN,
        grid.addVector(GridTools.DOWN, GridTools.LEFT), #down-left
        GridTools.LEFT
    ]

    vects = [grid.addVector((x, y), z) for z in dirs]

    adjacent_count = 0
    for vect in vects: 
        res = grid.gridAtVector(vect)
        if res is not None and res != '.':
            adjacent_count += 1
            
    return adjacent_count

total_rolls = 0
for i in range(grid.rows()):
    for j in range(grid.cols()):
        if grid.grid[i][j] != '.':
            res = count_adjacent(i, j)
            if res < 4:
                total_rolls += 1
            

grid.printGrid()
print(total_rolls)

pt2_total_rolls = 0
moved_rolls = 1
import time
while moved_rolls > 0:
    moved_rolls = 0
    for i in range(grid.rows()):
        for j in range(grid.cols()):
            if grid.grid[i][j] != '.':
                res = count_adjacent(i, j)
                if res < 4:
                    pt2_total_rolls += 1
                    moved_rolls += 1
                    grid.grid[i][j] = 'x'
    
    #creates kind of a cool animation in the terminal
    grid.printGrid()

    for i in range(grid.rows()):
        for j in range(grid.cols()):
            if grid.grid[i][j] == 'x':
                grid.grid[i][j] = '.'

print(total_rolls)
print(pt2_total_rolls)