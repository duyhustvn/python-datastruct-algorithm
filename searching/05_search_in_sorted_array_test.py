#!/usr/bin/env python3

from typing import List
import unittest


sl = __import__('05_search_in_sorted_array')

class Test:
    def __init__(self, nums: List[int], target: int, expectedOutput: int):
        self.nums = nums
        self.target = target
        self.expectedOutput = expectedOutput

class Unittest(unittest.TestCase):
    def testInSortedArray(self):
        tests = [
            Test([1], 0, -1),
            Test([1], 1, 0),
            Test([1], 2, -1),
            Test([1,3], 0, -1),
            Test([1,3], 1, 0),
            Test([1,3], 2, -1),
            Test([1,3], 3, 1),
            Test([1,3], 4, -1),
            Test([3,5,1], 0, -1),
            Test([4,6,8,9,0,1,3], -1, -1),
            Test([4,6,8,9,0,1,3], 0, 4),
            Test([4,6,8,9,0,1,3], 1, 5),
            Test([4,6,8,9,0,1,3], 2, -1),
            Test([4,6,8,9,0,1,3], 3, 6),
            Test([4,6,8,9,0,1,3], 5, -1),
            Test([4,6,8,9,0,1,3], 6, 1),
            Test([4,6,8,9,0,1,3], 7, -1),
            Test([4,6,8,9,0,1,3], 8, 2),
        ]

        for test in tests:
            solution = sl.Solution()
            result = solution.search(test.nums, test.target)
            self.assertEqual(result, test.expectedOutput)

if __name__ == '__main__':
    unittest.main()
