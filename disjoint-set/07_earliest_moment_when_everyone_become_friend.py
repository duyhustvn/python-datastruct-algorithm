# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

"""
[[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
6
[[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]
4
[[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4]]
6
[[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]]
4
"""

class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size 

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x 
        
        rootX = self.find(self.root[x])
        self.root[x] = rootX 
        return rootX 
    
    def union(self, x: int, y: int):
        rootX = self.root[x]
        rootY = self.root[y]

        if rootX != rootY:
            if self.rank[x] > self.rank[y]:
                self.root[rootY] = rootX 
            elif self.rank[x] == self.rank[y]:
                self.root[rootY] = rootX 
                self.rank[x] += 1
            else:
                self.root[rootX] = rootY 
    
    def findUniRoot(self, size: int) -> int:
        uniRoot = set() 
        for i in range(size):
            rootX = self.find(i)
            uniRoot.add(rootX)
        return len(uniRoot)


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        uf = UnionFind(n)

        for idx, log in enumerate(logs):
            uf.union(log[1], log[2])
            if uf.findUniRoot(n) == 1:
                return log[0]
        return -1
