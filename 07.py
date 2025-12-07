from GridTools import GridTools

with open("inputs/07.txt") as file:
    lines = [x.strip() for x in file.readlines()]

grid = GridTools(gridLines=lines)

pt1_total = 0
for row in range(grid.rows()):
    for col in range(grid.cols()):
        cur = grid.gridAtVector((row, col))
        above = grid.gridAtVector(grid.addVector((row, col), GridTools.UP))
        if above == "|" or above == "S":
            if cur == "^":
                # set left and right
                pt1_total += 1
                left = grid.addVector((row, col), GridTools.LEFT)
                right = grid.addVector((row, col), GridTools.RIGHT)
                if grid.gridAtVector(left):
                    grid.grid[left[0]][left[1]] = "|"
                if grid.gridAtVector(right):
                    grid.grid[right[0]][right[1]] = "|"
            else:
                grid.grid[row][col] = "|"

print(pt1_total)

# reset grid
grid = GridTools(gridLines=lines)
# find starting position
i = 0
while True:
    if grid.grid[0][i] == "S":
        break
    i += 1

memo = {}


def rec_count_tachyons(pos):
    # base case: we're in the bottom row
    if pos[0] == grid.rows():
        return 1
    if pos in memo:
        return memo[pos]

    # else, check if we're at a splitter. if so spawn new tachyons to the left and right
    total = 0
    if grid.gridAtVector(pos) == "^":
        left = grid.addVector(pos, GridTools.LEFT)
        right = grid.addVector(pos, GridTools.RIGHT)
        if grid.gridAtVector(left):
            total += rec_count_tachyons(left)
        if grid.gridAtVector(right):
            total += rec_count_tachyons(right)

    # else, we just move down
    else:
        total += rec_count_tachyons(grid.addVector(pos, GridTools.DOWN))

    memo[pos] = total
    return total


print(rec_count_tachyons((0, i)))
