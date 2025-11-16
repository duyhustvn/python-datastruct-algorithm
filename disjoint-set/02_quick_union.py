class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]

    def find(self, idx: int) -> int:
        while idx != self.root[idx]:
            idx = self.root[idx]
        return idx

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[x] = rootY

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
