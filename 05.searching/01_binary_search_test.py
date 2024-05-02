#!/usr/bin/env python3

import unittest

bs = __import__('01_binary_search')

class TestBinarySearch(unittest.TestCase):
    def testBinarySearch(self):
        tests = [
            # nums target expectedOutput
            [[], 1, -1],
            [[1], 1, 0],
            [[1], 2, -1],
            [[1, 2], 0, -1],
            [[1, 2], 1, 0],
            [[1, 2], 2, 1],
            [[1, 2], 3, -1],
            [[1, 2, 3], 0, -1],
            [[1, 2, 3], 1, 0],
            [[1, 2, 3], 2, 1],
            [[1, 2, 3], 3, 2],
            [[1, 2, 3], 4, -1],
            [[1, 3, 4, 5, 7, 9, 12, 14, 16], 0, -1],
            [[1, 3, 4, 5, 7, 9, 12, 14, 16], 1, 0],
            [[1, 3, 4, 5, 7, 9, 12, 14, 16], 9, 5],
            [[1, 3, 4, 5, 7, 9, 12, 14, 16], 14, 7],
            [[1, 3, 4, 5, 7, 9, 12, 14, 16], 16, 8],
            [[1, 3, 4, 5, 7, 9, 12, 14, 16], 17, -1],
        ]

        for test in tests:
            idx = bs.binary_search(test[0], test[1])
            self.assertEqual(idx, test[2])

if __name__ == '__main__':
    unittest.main()
