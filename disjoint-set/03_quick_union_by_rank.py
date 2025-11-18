class UnionFind:
    def __init__(self, size: int):
        self.root = [(i,1) for i in range(size)]
    
    def union(self, x: int, y: int):
        # Time complexty: O(logN)
        # it use find method 
        rootX, heighX = self.find(x)
        rootY, heighY = self.find(y)
        if rootX != rootY:
            if heighX > heighY:
                self.root[rootY] = (rootX, heighX)
            elif heighX == heighY:
                self.root[rootY] = (rootX, heighX+1)
            else:
                self.root[rootX] = (rootY, heighY)

    # find root of index idx
    def find(self, idx: int) -> (int,int):
        # Time complexity: O(logN) 
        # logN: is the heigh of union-find
        while True:
            rootIdx, heigh = self.root[idx]
            if rootIdx == idx:
                return idx, heigh
            idx = rootIdx
        return -1, -1
                

    def connected(self, x: int, y: int) -> bool:
        # Time complexity: O(logN)
        # it use find method 
        rootX, heighX = self.find(x)
        rootY, heighY = self.find(y)
        return rootX == rootY
    
    
