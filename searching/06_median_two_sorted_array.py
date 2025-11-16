#!/usr/bin/env python3

# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List
"""
[1,3]
[2]
[1,2]
[3,4]
[1,2,3,4,5,6]
[3,4]
[1,2,3,12,13,56]
[3,4,23,25,36,38]
[1,2,3,12,13,56]
[3,4,23,25,36]
"""
class Solution:
    def mergeThenFindMedian(self, nums1: List[int], nums2: List[int]) -> float:
        """
        TC: O(n+m)
        SC: O(n+m)
        """
        mergedNums = []
        i = j = 0
        s1=len(nums1)
        s2=len(nums2)
        while i < s1 and j < s2:
            if nums1[i] <= nums2[j]:
                mergedNums.append(nums1[i])
                i+=1
            else:
                mergedNums.append(nums2[j])
                j+=1
        while i < s1:
            mergedNums.append(nums1[i])
            i+=1
        while j < s2:
            mergedNums.append(nums2[j])
            j+=1
        
        mid = (s1 + s2) // 2
        
        if (s1+s2)%2 == 0:
            return (mergedNums[mid] + mergedNums[mid-1])/2
        else:
            return mergedNums[mid]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return self.mergeThenFindMedian(nums1, nums2)
        return self.bsRecursive(nums1, nums2)

    def bsRecursive(self, nums1: List[int], nums2: List[int]) -> float:
        """
        TC: O(logm + logn) = O(log(m*n))
        SC: O(logm + logn) = O(log(m*n))
        """
        n1 = len(nums1)
        n2 = len(nums2)

        def bs(k: int, a_start: int, a_end: int, b_start: int, b_end: int) -> int:
            if a_start > a_end:
                return nums2[k-a_start]
            if b_start > b_end:
                return nums1[k-b_start]

            a_mid = (a_start + a_end)//2
            b_mid = (b_start + b_end)//2 

            if a_mid + b_mid < k:
                # remove the smallest half part 
                if nums1[a_mid] < nums2[b_mid]:
                    return bs(k, a_mid+1, a_end, b_start, b_end)
                else:
                    return bs(k, a_start, a_end, b_mid+1, b_end)
            else:
                # remove largest half part
                if nums1[a_mid] < nums2[b_mid]:
                    return bs(k, a_start, a_end, b_start, b_mid-1)
                else:
                    return bs(k, a_start, a_mid-1, b_start, b_end)

        mid = (n1+n2)//2
        if (n1+n2)%2 == 1:
            return bs(mid, 0, n1-1, 0, n2-1)
        else:
            return (bs(mid, 0, n1-1, 0, n2-1) + bs(mid-1, 0, n1-1, 0, n2-1))/2
