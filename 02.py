import re

# read input
with open("inputs/02.txt") as f:
    lines = [x.strip() for x in f.readlines()]

input = lines[0]

ranges = [(int(id.split("-")[0]), int(id.split("-")[1]) + 1) for id in input.split(",")]

pt1_regex = re.compile(r"(.+)\1")
pt2_regex = re.compile(r"(.+)\1+")


def is_invalid(id, regex):
    if regex.fullmatch(id):
        return True
    else:
        return False


pt1_ans = 0
pt2_ans = 0
for range_list in ranges:
    for i in range(*range_list):
        str_i = str(i)
        if is_invalid(str_i, pt1_regex):
            pt1_ans += i
        if is_invalid(str_i, pt2_regex):
            pt2_ans += i

print(pt1_ans)
print(pt2_ans)
