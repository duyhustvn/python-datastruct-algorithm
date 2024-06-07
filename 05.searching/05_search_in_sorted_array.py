#!/usr/bin/env python3

# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List

class Solution:
    """
    Time complexity: O(logN)
    Space complexity: O(1)
    """
    def bs(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1

    #  [4,5,1,2,3] 6
    def findPivot(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        right = n-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > nums[n-1]:
                left = mid + 1
            else:
                right = mid - 1
        return left


    def search(self, nums: List[int], target: int) -> int:
        # find the rotate index

        pivot = self.findPivot(nums)

        if target == nums[pivot]:
            return pivot

        if (answer := self.bs(nums, 0, pivot-1, target)) != -1:
            return answer
        return self.bs(nums, pivot, len(nums)-1, target)
