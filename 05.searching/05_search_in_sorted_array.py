#!/usr/bin/env python3

# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List

class Solution:
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

    def search(self, nums: List[int], target: int) -> int:
        # find the rotate index
        left = 0
        right = len(nums)-1
        pivot = len(nums)-1

        if len(nums) == 1:
            pivot = 0
        elif len(nums) == 2:
                pivot = 1
        elif nums[0] < nums[right]: # array not rotate
            pivot = len(nums)-1
        else:
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return mid

                if mid == 0:
                    pivot = 1
                    break
                elif mid == len(nums)-1 or nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                    pivot = mid
                    break
                elif nums[mid] > nums[0]:
                    left = mid+1
                else:
                    right = mid -1


        if target == nums[pivot]:
            return pivot

        if target >= nums[0]:
            return self.bs(nums, 0, pivot-1, target)
        else:
            return self.bs(nums, pivot, len(nums)-1, target)
