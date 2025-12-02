#read input
with open("inputs/02.txt") as f:
    lines = [x.strip() for x in f.readlines()]

input = lines[0]

ranges = [(int(id.split('-')[0]), int(id.split('-')[1]) + 1) for id in input.split(',')]

import re
pt1_regex = re.compile(r'(.+)\1')
def is_invalid(id):
    if pt1_regex.fullmatch(id):
        return True
    else:
        return False

pt2_regex = re.compile(r'(.+)\1+')

def pt2_is_invalid(id):
    if pt2_regex.fullmatch(id):
        return True
    else:
        return False

invalid_ranges = 0
pt2_ans = 0
for range_list in ranges:
    for i in range(*range_list):
        if is_invalid(str(i)):
            invalid_ranges += i
            print(f'invalid: {i}')
        if pt2_is_invalid(str(i)):
            pt2_ans += i

print(invalid_ranges)
print(pt2_ans)
