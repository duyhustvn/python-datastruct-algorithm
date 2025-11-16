#!/usr/bin/env python3

# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) ->int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
