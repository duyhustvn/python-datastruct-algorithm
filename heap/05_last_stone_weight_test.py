#!/usr/bin/env python3

import os
import sys
from typing import List
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sl = __import__('05_last_stone_weight')


class Test:
    def __init__(self, stones: List[int], expectedOutput: int):
        self.stones = stones
        self.expectedOutput = expectedOutput


class TestLastStoneWeight(unittest.TestCase):
    def testLastStoneWeight(self):
        tests = [
            # stones, expectedOutput
            Test([2, 7, 4, 1, 8, 1], 1),
            Test([1], 1),
            Test([2, 2], 0),
            Test([3, 7, 2], 2),
            Test([1, 3], 2),
            Test([10, 4, 2, 10], 2),
            Test([7, 6, 7, 6, 9], 3),
            Test([1, 1, 1, 1], 0),
            Test([1, 1, 1], 1),
            Test([31, 26, 33, 21, 40], 9),
            Test([1000], 1000),
            Test([100, 50, 50], 0),
        ]

        for test in tests:
            solution = sl.Solution()
            result = solution.lastStoneWeight(test.stones.copy())
            self.assertEqual(result, test.expectedOutput)


if __name__ == '__main__':
    unittest.main()
