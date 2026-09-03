#!/usr/bin/env python3

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def maxHeapFn(matrix: List[List[int]], k: int) -> int:
            # Time complexity: O(mnlogk)
            # Space complexity: O(k)
            maxHeap = []
            for row in matrix:
                for item in row:
                    heapq.heappush(maxHeap, -1 * item)
                    if len(maxHeap) > k:
                        heapq.heappop(maxHeap)
            return -1 * maxHeap[0]

        def minHeapFn(matrix: List[List[int]], k: int) -> int:
            # algo: the same idea with 2 pointer but using multiple pointer
            # and using minHeap to track pointer
            # Time complexity: X = min(k, N) O(x + klogx)
            # Space complexity: O(k)
            minHeap = []

            for i in range(min(len(matrix), k)):
                # heapq.heappush(minHeap, (matrix[i][0], i, 0))
                minHeap.append((matrix[i][0], i, 0))

            heapq.heapify(minHeap)

            while True:
                (v, i, j) = heapq.heappop(minHeap)
                if k == 1:
                    return v
                k -= 1
                if j + 1 >= len(matrix[0]):
                    continue
                heapq.heappush(minHeap, (matrix[i][j + 1], i, j + 1))

        return minHeapFn(matrix, k)
