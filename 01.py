#read input
with open("inputs/01.txt") as f:
    lines = [x.strip() for x in f.readlines()]

dial = 50
total_zeros = 0

for line in lines:
    dir = line[0]
    number = int(line[1:])

    mod = -1 if dir == 'L' else 1

    dial += number * mod
    dial %= 100

    if dial == 0:
        total_zeros += 1

print(total_zeros)