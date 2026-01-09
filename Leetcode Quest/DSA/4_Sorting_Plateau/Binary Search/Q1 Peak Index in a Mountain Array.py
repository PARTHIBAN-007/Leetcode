"""
Peak Index in a Mountain Array

You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

 

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

Example 3:

Input: arr = [0,10,5,2]

Output: 1

 

Constraints:

3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.

"""
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        if arr[0]>arr[1]:
            return arr[0]
        if arr[n-1]>arr[n-2]:
            return arr[n-1]
        
        l , r = 1, n-2
        
        while l<=r:
            m = (l+r)//2
            if arr[m-1]<arr[m]>arr[m+1]:
                return m
            elif arr[m-1]<arr[m]:
                l = m+1
            else:
                r = m-1
        return -1