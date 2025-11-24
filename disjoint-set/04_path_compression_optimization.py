class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def union(self, x: int, y: int):
        # Time complexty: O(logN)
        # it use find method 
        rootX = self.find(x)
        rootY = self.find(y)

        heighX = self.rank[x]
        heighY = self.rank[y]

        if rootX != rootY:
            if heighX > heighY:
                self.root[rootY] = rootX
            elif heighX == heighY:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            else:
                self.root[rootX] = rootY

    # find root of index idx
    def find(self, idx: int) -> int:
        # Time complexity: O(logN) consider to be O(1)
        # logN: is the heigh of union-find
        # https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Time_complexity
        if idx == self.root[idx]:
            return idx
        
        rootIdx = self.find(self.root[idx])
        self.root[idx] = rootIdx
        return rootIdx
        

    def connected(self, x: int, y: int) -> bool:
        # Time complexity: O(logN)
        # it use find method 
        rootX = self.find(x)
        rootY = self.find(y)
        return rootX == rootY
    
    
