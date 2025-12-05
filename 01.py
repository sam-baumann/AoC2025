# read input
with open("inputs/01.txt") as f:
    lines = [x.strip() for x in f.readlines()]

dial = 50
total_zeros = 0
pt2 = 0

for line in lines:
    dir = line[0]
    number = int(line[1:])

    mod = -1 if dir == "L" else 1

    pt2_dial = dial
    dial += number * mod

    dial %= 100

    if dial == 0:
        total_zeros += 1

    for num in range(number):
        pt2_dial += 1 * mod
        pt2_dial %= 100

        if pt2_dial == 0:
            pt2 += 1

print(total_zeros)
print(pt2)
