#!/usr/bin/env python3

# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/

import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Time complexy: O(m * logn + m .logk) = O(mlognk)
        # Space complexity: O(k)

        def binary_search(row):
            low, high = 0, len(row)
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low

        result = []
        maxHeap = []
        for rowIdx, row in enumerate(mat):
            numSoliders = binary_search(row)
            heapq.heappush(maxHeap, (-1 * numSoliders, -1 * rowIdx))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        while len(maxHeap) > 0:
            (numSoliders, rowIdx) = heapq.heappop(maxHeap)
            result.insert(0, -1 * rowIdx)

        return result
