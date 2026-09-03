#!/usr/bin/env python3

import os
import sys
from typing import List
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sl = __import__('07_kth_smallest_element_in_sorted_matrix')


class Test:
    def __init__(self, matrix: List[List[int]], k: int, expectedOutput: int):
        self.matrix = matrix
        self.k = k
        self.expectedOutput = expectedOutput


class TestKthSmallest(unittest.TestCase):
    def testKthSmallest(self):
        tests = [
            # Standard LeetCode Example 1
            Test(
                [
                    [1, 5, 9],
                    [10, 11, 13],
                    [12, 13, 15],
                ],
                8,
                13,
            ),
            # Standard LeetCode Example 2: 1x1 matrix with negative number
            Test([[-5]], 1, -5),
            # 1x1 matrix with 0 and positive numbers
            Test([[0]], 1, 0),
            Test([[42]], 1, 42),
            # Minimum k (k = 1) -> top-left element
            Test(
                [
                    [1, 5, 9],
                    [10, 11, 13],
                    [12, 13, 15],
                ],
                1,
                1,
            ),
            # Maximum k (k = n^2) -> bottom-right element
            Test(
                [
                    [1, 5, 9],
                    [10, 11, 13],
                    [12, 13, 15],
                ],
                9,
                15,
            ),
            # 2x2 matrix
            Test(
                [
                    [1, 2],
                    [3, 4],
                ],
                3,
                3,
            ),
            # Matrix with all identical elements
            Test(
                [
                    [7, 7, 7],
                    [7, 7, 7],
                    [7, 7, 7],
                ],
                5,
                7,
            ),
            # Matrix with duplicates
            Test(
                [
                    [1, 2],
                    [1, 3],
                ],
                1,
                1,
            ),
            Test(
                [
                    [1, 2],
                    [1, 3],
                ],
                2,
                1,
            ),
            Test(
                [
                    [1, 2],
                    [1, 3],
                ],
                4,
                3,
            ),
            # Matrix with all negative numbers
            Test(
                [
                    [-10, -8, -6],
                    [-7, -5, -3],
                    [-4, -2, -1],
                ],
                5,
                -5,
            ),
            # Mixed positive, zero, negative
            Test(
                [
                    [-5, -4],
                    [-1, 2],
                ],
                3,
                -1,
            ),
            # 4x4 matrix with various k
            Test(
                [
                    [1, 4, 7, 11],
                    [2, 5, 8, 12],
                    [3, 6, 9, 16],
                    [10, 13, 14, 17],
                ],
                5,
                5,
            ),
            Test(
                [
                    [1, 4, 7, 11],
                    [2, 5, 8, 12],
                    [3, 6, 9, 16],
                    [10, 13, 14, 17],
                ],
                10,
                10,
            ),
            Test(
                [
                    [1, 4, 7, 11],
                    [2, 5, 8, 12],
                    [3, 6, 9, 16],
                    [10, 13, 14, 17],
                ],
                15,
                16,
            ),
            Test(
                [
                    [1, 4, 7, 11],
                    [2, 5, 8, 12],
                    [3, 6, 9, 16],
                    [10, 13, 14, 17],
                ],
                16,
                17,
            ),
            # Matrix with large gap between rows
            Test(
                [
                    [1, 2, 3],
                    [10, 20, 30],
                    [100, 200, 300],
                ],
                4,
                10,
            ),
            # Rectangular matrix (2x3 and 3x2)
            Test(
                [
                    [1, 3, 5],
                    [2, 4, 6],
                ],
                4,
                4,
            ),
            Test(
                [
                    [1, 4],
                    [2, 5],
                    [3, 6],
                ],
                5,
                5,
            ),
        ]

        for test in tests:
            solution = sl.Solution()
            result = solution.kthSmallest([row.copy() for row in test.matrix], test.k)
            self.assertEqual(result, test.expectedOutput)


if __name__ == '__main__':
    unittest.main()
