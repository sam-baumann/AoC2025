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

#apply coordinate_compression
#we start by sorting the coordinates left-to-right (x direction) 
compressed_x = sorted(list(set([x[0] for x in coords_list])))
compressed_y = sorted(list(set([x[1] for x in coords_list])))

compressed_coords = [(compressed_x.index(i), compressed_y.index(j)) for (i, j) in coords_list]

def get_original_coord(compressed_coord):
    return (compressed_x[compressed_coord[0]], compressed_y[compressed_coord[1]])

max_x = max([x[0] for x in compressed_coords]) + 1
max_y = max([x[1] for x in compressed_coords]) + 1

grid = GridTools(grid=[['.' for _ in range(max_y)] for _ in range(max_x)])

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

for coord, next in zip(compressed_coords, compressed_coords[1:]):
    print(grid[coord])
    draw_line(coord, next)
    grid[coord] = '0'

#now connect last and first
draw_line(compressed_coords[-1], compressed_coords[0])
grid[compressed_coords[-1]] = '0'

#TODO something is wrong here I think
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
        if grid[i][j] != 'x' and grid[i][j] != '0':
            crossings = count_crossings((i, j), None)
            crossings = 'z' if crossings % 2 == 0 else str(crossings)
            grid[i][j] = crossings
            print(f'done with point {(i, j)}')

#iterate over every possible rect again, but trace the perimiter and check it doesn't cross
cur_max = 0
for i, coord1 in enumerate(compressed_coords):
    for coord2 in compressed_coords[i+1:]:
        xs = sorted([x for x in zip(coord1, coord2)][0])
        ys = sorted([x for x in zip(coord1, coord2)][1])

        #trace the perimeter
        last = '0'
        perimeter_coords = [
            [(x, ys[0]) for x in range(xs[0], xs[1])], #top-left - top-right
            [(xs[0], y) for y in range(ys[0], ys[1])], #top-right - bottom-right
            [(x, ys[1]) for x in range(xs[0], xs[1])], #bottom-right - bottom-left
            [(xs[1], y) for y in range(ys[0], ys[1])], #bottom-left - top-left
        ]

        if not any([grid[coord] == 'z' for x in perimeter_coords for coord in x]):
            coord1_uncompressed = get_original_coord(coord1)
            coord2_uncompressed = get_original_coord(coord2)
            x = abs(coord2_uncompressed[0] - coord1_uncompressed[0]) + 1
            y = abs(coord2_uncompressed[1] - coord1_uncompressed[1]) + 1
            if x * y > cur_max:
                print(f'New max from coords: {coord1_uncompressed}, {coord2_uncompressed}: {x * y}')
            cur_max = max(x * y, cur_max)

print(grid)
print(cur_max)