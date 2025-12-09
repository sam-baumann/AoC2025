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
        return self.id
