import re
with open("inputs/10.txt") as f:
    lines = [x.strip() for x in f.readlines()]

goals = []
diagrams = [[] for _ in range(len(lines))]
for i, line in enumerate(lines):
    close = line.index(']')
    #convert to binary
    goalnum = 0
    for j, ch in enumerate(line[1:close]):
        if ch == '#':
            goalnum |= 1 << j 
    goals.append(goalnum)

    #grab all numbers with regex
    groups_regex = re.compile(r"\(((?:\d,?)+)\)")
    for group in groups_regex.findall(line):
        curnum = 0
        for shift in [int(x) for x in group.split(',')]:
            curnum |= 1 << shift
        diagrams[i].append(curnum)

def button_press_seq(goalnum:int, diagrams:list[int]):
    #base case: goalnum is in diagrams
    if goalnum in diagrams:
        return 1

    #otherwise, try all options
    ret = []
    for i, diagram in enumerate(diagrams):
        ret.append(button_press_seq(goalnum ^ diagram, diagrams[i+1:])) 
    if len(ret) == 0:
        return 100
    else:
        return min(ret) + 1

print(sum([button_press_seq(goal, diagram) for goal, diagram in zip(goals, diagrams)]))