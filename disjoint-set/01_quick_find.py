class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, idx: int) -> int:
        return self.root[idx]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # find all the node that has root is rootY 
            # then set it to rootX 
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
