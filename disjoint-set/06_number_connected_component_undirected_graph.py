# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

"""
2
[[0,1]]
5
[[0,1],[3,4]]
5
[[0,1],[1,2],[3,4]]
5
[[0,1],[1,2],[2,3],[3,4]]
"""

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x  
        rootX = self.find(self.root[x])
        self.root[x] = rootX 
        return rootX 
    def union(self, x: int, y: int): 
        rootX = self.find(x) 
        rootY = self.find(y) 

        if rootX != rootY:
            if self.rank[x] > self.rank[y]:
                self.root[rootY] = rootX 
            elif self.rank[x] > self.rank[y]:
                self.root[rootY] = rootX 
                self.rank[x] += 1 
            else:
                self.root[rootX] = rootY
    def findUniqueRoot(self, size: int):
        rootSet = set() 
        for i in range(size):
            rootI = self.find(i) 
            rootSet.add(rootI) 
        return rootSet

class Solution:
    """
    Time complexity: O(1)
    Space complexity: O(n)
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        rootSet = uf.findUniqueRoot(n)
        return len(rootSet)
