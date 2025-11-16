#!/usr/bin/env python3

import unittest

bs = __import__('01_binary_search')

class Test:
    def __init__(self, arr, target, expectedOutput):
        self.arr = arr
        self.target = target
        self.expectedOutput = expectedOutput


class TestBinarySearch(unittest.TestCase):
    def testBinarySearch(self):
        tests = [
            # nums target expectedOutput
            Test([], 1, -1),
            Test([1], 1, 0),
            Test([1], 2, -1),
            Test([1, 2], 0, -1),
            Test([1, 2], 1, 0),
            Test([1, 2], 2, 1),
            Test([1, 2], 3, -1),
            Test([1, 2, 3], 0, -1),
            Test([1, 2, 3], 1, 0),
            Test([1, 2, 3], 2, 1),
            Test([1, 2, 3], 3, 2),
            Test([1, 2, 3], 4, -1),
            Test([1, 3, 4, 5, 7, 9, 12, 14, 16], 0, -1),
            Test([1, 3, 4, 5, 7, 9, 12, 14, 16], 1, 0),
            Test([1, 3, 4, 5, 7, 9, 12, 14, 16], 9, 5),
            Test([1, 3, 4, 5, 7, 9, 12, 14, 16], 14, 7),
            Test([1, 3, 4, 5, 7, 9, 12, 14, 16], 16, 8),
            Test([1, 3, 4, 5, 7, 9, 12, 14, 16], 17, -1),
        ]

        for test in tests:
            idx = bs.binary_search(test.arr, test.target)
            self.assertEqual(idx, test.expectedOutput)

if __name__ == '__main__':
    unittest.main()
