from GridTools import GridTools

with open("inputs/09_ex.txt") as f:
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

#scan across the grid, and track the component rectangles
rectangles = []
cur_tracking_rectangles = {}
for rownum, row in enumerate(grid.grid):
    signals = []
    cur_tracking = True
    for i, col in enumerate(row):
        if col == '0':
            signals.append(('0', i))
            cur_tracking = not cur_tracking
        if col == 'x' and cur_tracking:
            signals.append(('x', i))
    print(row, signals)

print(rectangles)


