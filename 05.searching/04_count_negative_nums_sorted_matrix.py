#!/usr/bin/env python3
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

from typing import List


class Solution:
    def findFistNegativeNum(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        while left <= right:
            mid = left + (right-left)//2
            if arr[mid] >= 0:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def countNegativesBinarySearch(self, grid: List[List[int]]) -> int:
        cnt = 0
        for g in grid:
            idx = self.findFistNegativeNum(g)
            cnt += len(grid[0]) - idx
        return cnt

    def countNegatives(self, grid: List[List[int]]) -> int:
       return self.countNegativesBinarySearch(grid)
