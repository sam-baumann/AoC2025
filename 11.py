from math import prod

with open("inputs/11.txt") as f:
    lines = [x.strip() for x in f.readlines()]

graph = {}
for line in lines:
    graph[line[:3]] = line[4:].split()

graph["out"] = []

# used DFS to determine input graph is acyclic. Good, now let's use DFS to find all paths
memo = {x: {} for x in graph.keys()}


def DFS(v, dest):
    # base case: v is 'out'
    if v == dest:
        return 1
    if dest in memo[v]:
        return memo[v][dest]

    # else, run DFS on all neighbors and return their sum
    ret = sum(DFS(w, dest) for w in graph[v])
    memo[v][dest] = ret
    return ret


if (
    "you" in graph
):  # this check only exists because the samples given in the problem statement are different
    print(DFS("you", "out"))

# potential paths:
#   svr -> dac -> fft -> out
#   svr -> fft -> dac -> out
if "svr" in graph:
    seq = ["svr", "fft", "dac", "out"]
    pt2_sum = prod([DFS(x, y) for x, y in zip(seq, seq[1:])])

    seq = ["svr", "dac", "fft", "out"]
    pt2_sum += prod([DFS(x, y) for x, y in zip(seq, seq[1:])])

    print(pt2_sum)
