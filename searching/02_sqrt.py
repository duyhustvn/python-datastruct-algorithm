#!/usr/bin/env python3

# https://leetcode.com/problems/sqrtx/solution/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left = 0
        right = x//2
        while left <= right:
            mid = left + (right-left)//2
            if mid * mid == x:
                return mid

            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
