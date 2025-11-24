# https://leetcode.com/problems/number-of-provinces/description/

"""
Test Cases
[[1]]
[[1,1,0],[1,1,0],[0,0,1]]
[[1,0,0],[0,1,0],[0,0,1]]
"""

class UnionFind:
    def __init__(self, size: int) -> int:
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def union(self, x: int, y: int):
        """
        Time complexity: O(log) consider to be O(1)
        Look at find function to know why
        """
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[x] > self.rank[y]:
                self.root[rootY] = rootX
            elif self.rank[x] == self.rank[y]:
                self.root[rootY] = rootX
                self.rank[x] += 1
            else:
                self.root[rootX] = rootY
        
    # find the root of index x
    def find(self, x: int) -> int:
        """
        Time complexity: O(logN) consider to be O(1)
        logN: is the heigh of union-find
        https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Time_complexity
        """
        if x == self.root[x]:
            return x
        
        rootX = self.find(self.root[x])
        self.root[x] = rootX
        return rootX
    
    # find root 
    def findRoot(self, size: int):
        rootSet = set()
        for i in range(size):
            rootI = self.find(i)
            rootSet.add(rootI)
        return rootSet


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Time complexity: O(N^2)
        Space complexity: O(N)
        """
        n = len(isConnected)

        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        

        rootSet = uf.findRoot(n)
        return len(rootSet)
