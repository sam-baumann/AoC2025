from math import sqrt, prod


# disjoint set data structure should help with this problem
class DisjointSet:
    """
    Disjoint Set class based on wikipedia pseudocode implementations https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    """

    def __init__(self, id: str) -> None:
        self.id = id
        self.parent = self
        self.size = 1

    def find(self):
        x = self
        while x.parent is not x:
            (x, x.parent) = (x.parent, x.parent.parent)
        return x

    def union(self, other: "DisjointSet"):
        x = self.find()
        y = other.find()

        if x is y:
            return

        if x.size < y.size:
            (x, y) = (y, x)

        y.parent = x
        x.size += y.size

    def __repr__(self) -> str:
        if self is self.parent:
            return f"id: {self.id}"
        return f"id: {self.id}, parent: {self.find()}"


with open("inputs/08.txt") as f:
    lines = [x.rstrip() for x in f.readlines()]


def euclidian_distance(pt1, pt2):
    pt1 = [int(x) for x in pt1.split(",")]
    pt2 = [int(x) for x in pt2.split(",")]
    diff = [x - y for x, y in zip(pt1, pt2)]
    squared = sum([x**2 for x in diff])
    return sqrt(squared)


forest = {x: DisjointSet(x) for x in lines}

distances = {}
# find the distance between each point
for i, line1 in enumerate(lines):
    for line2 in lines[i + 1 :]:
        distance = euclidian_distance(line1, line2)
        distances[distance] = distances.get(distance, []) + [(line1, line2)]

ordered_pairs = [
    item for x in sorted(distances.items(), key=lambda x: x[0]) for item in x[1]
]

limit = 1000
for pair in ordered_pairs[:limit]:
    forest[pair[0]].union(forest[pair[1]])

# get the size of every disjoint set
sizes = {}
for line in lines:
    cur = forest[line].find()
    sizes[cur] = cur.size

sizes = [x[1] for x in sorted(sizes.items(), key=lambda x: x[1], reverse=True)]
topn = 3
print(sizes)
print(prod(sizes[:topn]))

# now we continue until all boxes are connected
goal_size = len(lines)
for pair in ordered_pairs[limit:]:
    forest[pair[0]].union(forest[pair[1]])
    if forest[pair[0]].find().size >= goal_size:
        # get x coords
        ans = int(pair[0].split(",")[0]) * int(pair[1].split(",")[0])
        print(pair)
        print(ans)
        break
