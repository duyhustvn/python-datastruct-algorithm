#!/usr/bin/env python3

# https://leetcode.com/problems/last-stone-weight/description/

"""
Test cases

[2,7,4,1,8,1]
[1]
[2,2]
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = -1 * heapq.heappop(maxHeap)
            y = -1 * heapq.heappop(maxHeap)
            if x == y:
                continue
            z = x - y
            heapq.heappush(maxHeap, -1 * z)
        return -1 * maxHeap[0] if len(maxHeap) >= 1 else 0
