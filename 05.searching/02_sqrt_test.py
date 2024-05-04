#!/usr/bin/env python3

import unittest

bs = __import__('02_sqrt')

class Test:
    def __init__(self, input, expectedOutput):
        self.input = input
        self.expectedOutput = expectedOutput



class TestBinarySearch(unittest.TestCase):
    def testMySqrt(self):
        tests = [
            # num expectedOutput
            Test(0, 0),
            Test(1, 1),
            Test(2, 1),
            Test(3, 1),
            Test(4, 2),
            Test(5, 2),
            Test(6, 2),
            Test(7, 2),
            Test(8, 2),
            Test(9, 3),
            Test(10, 3),
            Test(7768687, 2787),
            Test(776868743, 27872),
        ]

        for test in tests:
             solution = bs.Solution()
             result = solution.mySqrt(test.input)
             self.assertEqual(result, test.expectedOutput)

if __name__ == '__main__':
    unittest.main()
