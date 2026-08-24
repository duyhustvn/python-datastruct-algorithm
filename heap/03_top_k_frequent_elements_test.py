#!/usr/bin/env python3

import os
import sys
from typing import List
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sl = __import__('03_top_k_frequent_elements')


class Test:
    def __init__(self, nums: List[int], k: int, expectedOutput: List[int]):
        self.nums = nums
        self.k = k
        self.expectedOutput = expectedOutput


class TestTopKFrequent(unittest.TestCase):
    def testTopKFrequent(self):
        tests = [
            # nums, k, expectedOutput
            Test([1, 1, 1, 2, 2, 3], 2, [1, 2]),
            Test([1], 1, [1]),
            Test([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
            Test([-1, -1, -2, -2, -2, 0], 2, [-2, -1]),
            Test([7, 7, 7, 7], 1, [7]),
            Test([1, 2, 3], 3, [1, 2, 3]),
            Test([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3, [2, 3, 4]),
            Test([5, 5, 5, 6, 6, 7], 1, [5]),
            Test([5, 5, 5, 6, 6, 7], 2, [5, 6]),
            Test([0, 0, 0, 1, 1, 2], 2, [0, 1]),
            Test([-1, -1], 1, [-1]),
            Test([3, 0, 1, 0], 1, [0]),
        ]

        for test in tests:
            solution = sl.Solution()
            result = solution.topKFrequent(test.nums.copy(), test.k)
            self.assertCountEqual(result, test.expectedOutput)


if __name__ == '__main__':
    unittest.main()
