import re
import numpy as np
from scipy.optimize import LinearConstraint, milp

with open("inputs/10.txt") as f:
    lines = [x.strip() for x in f.readlines()]

goals = []
diagrams = [[] for _ in range(len(lines))]
joltage_reqs = [[] for _ in range(len(lines))]
for i, line in enumerate(lines):
    close = line.index("]")
    # convert to binary
    goalnum = 0
    for j, ch in enumerate(line[1:close]):
        if ch == "#":
            goalnum |= 1 << j
    goals.append(goalnum)

    # grab all numbers with regex
    groups_regex = re.compile(r"\(((?:\d,?)+)\)")
    for group in groups_regex.findall(line):
        curnum = 0
        for shift in [int(x) for x in group.split(",")]:
            curnum |= 1 << shift
        diagrams[i].append(curnum)

    joltage_reqs_regex = re.compile(r"\{(.*)\}")
    match = joltage_reqs_regex.search(line)
    if match:
        joltage_reqs[i] = [int(x) for x in match.group(1).split(",")]


def button_press_seq(goalnum: int, diagrams: list[int]):
    # base case: goalnum is in diagrams
    if goalnum in diagrams:
        return 1

    # otherwise, try all options
    ret = []
    for i, diagram in enumerate(diagrams):
        ret.append(button_press_seq(goalnum ^ diagram, diagrams[i + 1 :]))
    if len(ret) == 0:
        return 100
    else:
        return min(ret) + 1


print(sum([button_press_seq(goal, diagram) for goal, diagram in zip(goals, diagrams)]))

# formulate the pt 2 problem for scipy.optimize.milp
# b_u, b_l = joltage_req # the equation must match exactly so lower and upper bounds are the same
# A = buttons expressed as a matrix where the rows are each joltage requirement and the cols are the buttons that activate them
# c = np.ones_like(len(diagrams)) we need to minimize the sum of all decision variables, in this case the decision variables are the number of times to press a button
# integrality = c all vars must be integers

pt2_sum = 0
for diagram, reqs in zip(diagrams, joltage_reqs):
    A = np.array(
        [
            [int(x) for x in reversed(np.binary_repr(y, width=len(reqs)))]
            for y in diagram
        ]
    ).T
    constraint = LinearConstraint(A, reqs, reqs)  # pyright: ignore[reportArgumentType]
    c = np.ones(len(diagram))
    integrality = c
    res = milp(c=c, constraints=constraint, integrality=integrality)
    pt2_sum += sum(res.x)

print(pt2_sum)
