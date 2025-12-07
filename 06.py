from functools import reduce

with open("./inputs/06.txt") as f:
    lines = [x for x in f.readlines()]

pt1_lines = [x.strip().split() for x in lines]

# convert all but last to numbers
nums = [[int(x) for x in line] for line in pt1_lines[:-1]]
nums = [x for x in zip(*nums)]
operators = [
    {"+": lambda x, y: x + y, "*": lambda x, y: x * y}[x] for x in pt1_lines[-1]
]

total = 0
for num, operator in zip(nums, operators):
    total += reduce(operator, num)

print(total)

pt2_lines = [reduce(lambda x, y: x + y, x) for x in zip(*lines[:-1])]

i = 0
pt2_total = 0
for op in operators:
    # read left-to-right until there is a blank
    nums = []
    while True:
        try:
            nums.append(int(pt2_lines[i]))
            i += 1
        except ValueError:
            i += 1
            break
    pt2_total += reduce(op, nums)

print(pt2_total)
