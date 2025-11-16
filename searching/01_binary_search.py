#!/usr/bin/env python3

def binary_search(arr, target) -> int:
    """
    Binary search: find the index of target in the array (arr)
    """
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1
