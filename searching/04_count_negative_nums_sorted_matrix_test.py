#!/usr/bin/env python3

from typing import List
import unittest


sl = __import__('04_count_negative_nums_sorted_matrix')

class Test:
    def __init__(self, grid: List[List[int]], expectedOutput: int):
        self.grid = grid
        self.expectedOutput = expectedOutput

class Unittest(unittest.TestCase):
    def testCountNegativesBinarySearch(self):
        tests = [
            Test([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]], 8),
            Test([[0]], 0),
            Test([[-2]], 1),
            Test([[0, -2]], 1),
            Test([[0, -2], [-1, -2]], 3),
        ]

        for test in tests:
            solution = sl.Solution()
            result = solution.countNegativesBinarySearch(test.grid)
            self.assertEqual(result, test.expectedOutput)

if __name__ == '__main__':
    unittest.main()
