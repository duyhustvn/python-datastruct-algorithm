#!/usr/bin/env python3

# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq


class Solution:
    def findKthLargest(self, nums, k):
        # Time complexity: O(nlogk)
        # Space complexity: O(k)
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]
