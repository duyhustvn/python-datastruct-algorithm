#!/usr/bin/env python3

import unittest

sl = __import__('02_kth_largest_element_in_array')


class Test:
    def __init__(self, nums, k, expectedOutput):
        self.nums = nums
        self.k = k
        self.expectedOutput = expectedOutput


class TestKthLargestElement(unittest.TestCase):
    def testFindKthLargest(self):
        tests = [
            # nums, k, expectedOutput
            Test([3, 2, 1, 5, 6, 4], 2, 5),
            Test([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
            Test([1], 1, 1),
            Test([2, 2, 2, 2], 2, 2),
            Test([-1, -2, -3, -4, -5], 2, -2),
            Test([-1, 2, 0], 1, 2),
            Test([3, 2, 1, 5, 6, 4], 6, 1),
            Test([7, 10, 4, 3, 20, 15], 1, 20),
            Test([1, 2, 3, 4, 5], 3, 3),
            Test([5, 4, 3, 2, 1], 3, 3),
            Test([99, 99], 1, 99),
        ]

        for test in tests:
            solution = sl.Solution()
            result = solution.findKthLargest(test.nums.copy(), test.k)
            self.assertEqual(result, test.expectedOutput)


if __name__ == '__main__':
    unittest.main()
