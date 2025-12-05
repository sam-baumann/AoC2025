with open("./inputs/05.txt") as f:
    lines = [x.strip() for x in f.readlines()]

ranges = [] #list of tuples
ids = [] #list of numbers

i = 0
while len(lines[i]):
    ranges.append(tuple(int(x) for x in lines[i].split('-')))
    i += 1

i += 1
valid_nums = 0

while i < len(lines):
    num = int(lines[i])

    #check if num valid
    is_valid = False
    for range in ranges:
        if num >= range[0] and num <= range[1]:
            is_valid = True
            break

    if is_valid:
        valid_nums += 1
    
    i+= 1

print(valid_nums)

ranges = sorted(ranges, key = lambda x: x[0]) #sort by low end
new_ranges = []

#now, we can iterate over the ranges, merging them if the low end of the next range is lower than the high end of the current range
i = 0
while i < len(ranges):
    low, high = ranges[i]
    i += 1
    while not (i == len(ranges) or ranges[i][0] > high):
        high = max(high, ranges[i][1])
        i += 1
    new_ranges.append((low, high))

total = 0
for range in new_ranges:
    total += range[1] - range[0] + 1

print(total)
