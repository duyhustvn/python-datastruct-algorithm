#!/usr/bin/env python3

import unittest

quick_find = __import__('04_path_compression_optimization')
UnionFind = quick_find.UnionFind

class Test:
    def __init__(self):
        pass         

class TestQuickFind(unittest.TestCase):
    def testQuickFind(self):
        uf = UnionFind(20)
        uf.union(1, 2)
        uf.union(1, 3)
        uf.union(2, 5)
        uf.union(5, 6)
        uf.union(6, 7)
        uf.union(3, 8)
        uf.union(8, 9)

        result = uf.connected(1, 5)
        self.assertEqual(result, True)

        result = uf.connected(1, 2)
        self.assertEqual(result, True)

        result = uf.connected(1, 3)
        self.assertEqual(result, True)

        result = uf.connected(1, 4)
        self.assertEqual(result, False)

        result = uf.connected(5, 7)
        self.assertEqual(result, True)

        result = uf.connected(4, 9)
        self.assertEqual(result, False)

        uf.union(9, 4)
        result = uf.connected(4, 9)
        self.assertEqual(result, True)

        result = uf.connected(10, 9)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
