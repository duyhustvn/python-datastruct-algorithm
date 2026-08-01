#!/usr/bin/env python3

import heapq

# construct an empty Min Heap
minHeap = []
heapq.heapify(minHeap)

# construct a Heap with Initial values
# this process is call "Heapify"
# The Heap is a Min Heap
minHeapWithValues = [3, 1, 2]
heapq.heapify(minHeapWithValues)
# Insert an element to the Min Heap
heapq.heappush(minHeapWithValues, 6)
# Get top element from the Min Heap
# i.e. the smallest element
smallest = minHeapWithValues[0]
print(f"smallest before pop: {smallest}")
# Delete top element from Min Heap
smallest = heapq.heappop(minHeapWithValues)
print(f"smallest: {smallest}")
smallest = minHeapWithValues[0]
print(f"smallest after pop: {smallest}")

# Trick in constructing a Max Heap
# As there are no internal functions to construct a Max Heap
# We can multiply each element by -1, then heapify with these modified elements.
# The top element will be the smallest element in the modified set,
# It can also be converted to the maximum value in the original dataset.
maxHeap = [1, 2, 3]
maxHeap = [-x for x in maxHeap]
heapq.heapify(maxHeap)
# The top element of maxHeap is -3
# Convert -3 to 3, which is the maximum value in the original maxHeap
# Insert an element to the Max Heap
# Multiply the element by -1
# As we are converting the Min Heap to a Max Heap
heapq.heappush(maxHeap, -1 * 5)
# Get top element from the Max Heap
# i.e. the largest element
# When inserting an element, we multiplied it by -1
# Therefore, we need to multiply the element by -1 to revert it back
largest = -1 * maxHeap[0]
print(f"largest before pop: {largest}")
# Delete top element from the Max Heap
largets = heapq.heappop(maxHeap)
print(f"largest: {largest}")
largest = -1 * maxHeap[0]
print(f"largest after pop: {largest}")
