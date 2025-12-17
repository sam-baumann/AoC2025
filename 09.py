from GridTools import GridTools
from functools import cache

with open("inputs/09.txt") as f:
    lines = [x.strip() for x in f.readlines()]

coords_list = [tuple(int(y) for y in x.split(',')) for x in lines]
#consider all combinations of coords
cur_max = 0
for i, coord1 in enumerate(coords_list):
    for coord2 in coords_list[i+1:]:
        x = abs(coord2[0] - coord1[0]) + 1
        y = abs(coord2[1] - coord1[1]) + 1
        if x * y > cur_max:
            print(f'New max from coords: {coord1}, {coord2}')
        cur_max = max(x * y, cur_max)

print(cur_max)

max_x = max([x[0] for x in coords_list])
max_y = max([y[1] for y in coords_list])

grid = GridTools(grid=[['.' for _ in range (max_y + 1)] for _ in range(max_x + 1)])

def draw_line(start, end):
    if start[0] != end[0]:
        if start[0] > end[0]:
            start, end = (end, start)
        coords = [(x, start[1]) for x in range(start[0]+1, end[0])]
    else:
        if start[1] > end[1]:
            start, end = (end, start)
        coords = [(start[0], x) for x in range(start[1]+1, end[1])]

    for coord in coords:
        grid[coord] = 'x'

for coord, next in zip(coords_list, coords_list[1:]):
    print(grid[coord])
    draw_line(coord, next)
    grid[coord] = '0'

#now connect last and first
draw_line(coords_list[-1], coords_list[0])
grid[coords_list[-1]] = '0'
print(grid)

#precompute every square in the grid by drawing a ray to the right and counting crossings. recursive so we can cache results
@cache
def count_crossings(point, on_line):
    """
    Returns the number of 'x'es to the right of the current point. Only valid if initial point is a '.'
    
    :param point: Initial point
    :param on_line: internal tracking to avoid double counting lines
    """
    #base case: we are all the way to the right
    if point[1] >= grid.cols():
        return 0

    #now, check if we are on line
    cur = grid[point]
    right_vector = grid.addVector(point, GridTools.RIGHT)
    if cur == '0':
        #start tracking or complete tracking line
        if on_line is not None:
            if grid[grid.addVector(point, on_line)] == 'x':
                #we never exited, as this line curled back in the way it came from
                return count_crossings(right_vector, None)
            else:
                #we have now exited
                return 1 + count_crossings(right_vector, None)
        else: 
            dir = GridTools.UP if grid[grid.addVector(point, GridTools.UP)] == 'x' else GridTools.DOWN
            return count_crossings(right_vector, dir)
    elif on_line is None and cur == 'x':
        return 1 + count_crossings(right_vector, None)
    return count_crossings(right_vector, on_line)

for i in range(grid.rows()):
    for j in range(grid.cols()):
        if grid[i][j] == '.':
            crossings = count_crossings((i, j), None)
            crossings = 'z' if crossings == 0 else crossings
            grid[i][j] = crossings
            print(f'done with point {(i, j)}')

print(grid)


def line_crosses(perimeter_coords):
    last = '0'
    for coord in perimeter_coords:
        cur = grid[coord]
        if cur == 'x' and last == '.':
            return True
        last = cur

    return False

#iterate over every possible rect again, but trace the perimiter and check it doesn't cross
cur_max = 0
for i, coord1 in enumerate(coords_list):
    for coord2 in coords_list[i+1:]:
        xs = sorted([x for x in zip(coord1, coord2)][0])
        ys = sorted([x for x in zip(coord1, coord2)][1])

        #trace the perimeter
        last = '0'
        perimeter_coords = [
            [(x, ys[0]) for x in range(xs[0]+1, xs[1])], #top-left - top-right
            [(xs[0], y) for y in range(ys[0]+1, ys[1])], #top-right - bottom-right
            [(x, ys[1]) for x in range(xs[0]+1, xs[1])], #bottom-right - bottom-left
            [(xs[1], y) for y in range(ys[0]+1, ys[1])], #bottom-left - top-left
        ]

        if not any([line_crosses(x) for x in perimeter_coords]):
            x = abs(coord2[0] - coord1[0]) + 1
            y = abs(coord2[1] - coord1[1]) + 1
            if x * y > cur_max:
                print(f'New max from coords: {coord1}, {coord2}')
            cur_max = max(x * y, cur_max)

print(cur_max)