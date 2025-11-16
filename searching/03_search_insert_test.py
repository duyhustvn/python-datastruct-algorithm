#!/usr/bin/env python3
import unittest
from typing import List

sl = __import__('03_search_insert')

class Test:
    def __init__(self, nums: List[int], target: int, expectedOutput: int):
        self.nums = nums
        self.target = target
        self.expectedOutput = expectedOutput


class Unittest(unittest.TestCase):
    def testSearchInsert(self):
        tests = [
            # num expectedOutput
            Test([1], 0, 0),
            Test([1], 1, 0),
            Test([1], 2, 1),
            Test([1, 3, 4, 7, 9], 0, 0),
            Test([1, 3, 4, 7, 9], 1, 0),
            Test([1, 3, 4, 7, 9], 2, 1),
            Test([1, 3, 4, 7, 9], 6, 3),
            Test([1, 3, 4, 7, 9], 10, 5),
        ]

        for test in tests:
             solution = sl.Solution()
             result = solution.searchInsert(test.nums, test.target)
             self.assertEqual(result, test.expectedOutput)

if __name__ == '__main__':
    unittest.main()
