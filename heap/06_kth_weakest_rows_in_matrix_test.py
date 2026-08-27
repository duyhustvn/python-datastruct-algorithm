#!/usr/bin/env python3

import os
import sys
from typing import List
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sl = __import__('06_kth_weakest_rows_in_matrix')


class Test:
    def __init__(self, mat: List[List[int]], k: int, expectedOutput: List[int]):
        self.mat = mat
        self.k = k
        self.expectedOutput = expectedOutput


class TestKWeakestRows(unittest.TestCase):
    def testKWeakestRows(self):
        tests = [
            # Standard LeetCode Example 1
            Test(
                [
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1],
                ],
                3,
                [2, 0, 3],
            ),
            # Standard LeetCode Example 2
            Test(
                [
                    [1, 0, 0, 0],
                    [1, 1, 1, 1],
                    [1, 0, 0, 0],
                    [1, 0, 0, 0],
                ],
                2,
                [0, 2],
            ),
            # Single row with soldiers and civilians
            Test([[1, 1, 0]], 1, [0]),
            # Single row with only 0s
            Test([[0, 0, 0]], 1, [0]),
            # Single row with only 1s
            Test([[1, 1, 1]], 1, [0]),
            # Single element matrix [0] and [1]
            Test([[0]], 1, [0]),
            Test([[1]], 1, [0]),
            # Column vector (single column per row)
            Test(
                [[1], [0], [1], [0]],
                2,
                [1, 3],
            ),
            # Column vector with k equal to total rows
            Test(
                [[1], [0], [1], [0]],
                4,
                [1, 3, 0, 2],
            ),
            # All rows have same number of soldiers (ties broken by row index)
            Test(
                [
                    [1, 1],
                    [1, 1],
                    [1, 1],
                ],
                2,
                [0, 1],
            ),
            Test(
                [
                    [0, 0],
                    [0, 0],
                    [0, 0],
                ],
                3,
                [0, 1, 2],
            ),
            # Sorted in descending order (strongest to weakest)
            Test(
                [
                    [1, 1, 1],
                    [1, 1, 0],
                    [1, 0, 0],
                    [0, 0, 0],
                ],
                4,
                [3, 2, 1, 0],
            ),
            # Sorted in ascending order (weakest to strongest)
            Test(
                [
                    [0, 0, 0],
                    [1, 0, 0],
                    [1, 1, 0],
                    [1, 1, 1],
                ],
                3,
                [0, 1, 2],
            ),
            # k = 1 (only the single weakest row)
            Test(
                [
                    [1, 1, 1],
                    [1, 1, 0],
                    [1, 0, 0],
                ],
                1,
                [2],
            ),
            # Larger matrix with multiple tie breaks
            Test(
                [
                    [1, 1, 1, 0, 0],
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1],
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 0, 0],
                ],
                4,
                [1, 2, 4, 0],
            ),
        ]

        for test in tests:
            solution = sl.Solution()
            result = solution.kWeakestRows([row.copy() for row in test.mat], test.k)
            self.assertEqual(result, test.expectedOutput)


if __name__ == '__main__':
    unittest.main()
