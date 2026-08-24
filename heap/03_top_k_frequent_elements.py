#!/usr/bin/env python3

# https://leetcode.com/problems/top-k-frequent-elements/description/

import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time complexity: O(nlogk)
        # Space complexity: O(n)

        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        minHeap = []
        for key, value in frequencies.items():
            heapq.heappush(minHeap, (value, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        result = []
        while len(minHeap) > 0:
            item = heapq.heappop(minHeap)
            result.append(item[1])
        return result
