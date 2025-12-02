#read input
with open("inputs/02.txt") as f:
    lines = [x.strip() for x in f.readlines()]

input = lines[0]

ranges = [(int(id.split('-')[0]), int(id.split('-')[1]) + 1) for id in input.split(',')]

def is_invalid(id):
    len_is_even = (len(id) % 2) == 0
    if len_is_even:
        id_half = len(id) // 2
        if id[:id_half] == id[id_half:]:
            return True
    else:
        return False

invalid_ranges = 0
for range_list in ranges:
    for i in range(*range_list):
        if is_invalid(str(i)):
            invalid_ranges += i
            print(f'invalid: {i}')

print(invalid_ranges)