"""
K-Concatenation Maximum Sum

Given an integer array arr and an integer k, modify the array by repeating it k times.
For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].
Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.
As the answer can be very large, return the answer modulo 109 + 7.

 

Example 1:
Input: arr = [1,2], k = 3
Output: 9

Example 2:
Input: arr = [1,-2,1], k = 5
Output: 2

Example 3:
Input: arr = [-1,-2], k = 7
Output: 0
 

Constraints:

1 <= arr.length <= 105
1 <= k <= 105
-104 <= arr[i] <= 104

"""
from typing import List
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7

        def kadane(nums):
            cur = best = 0
            for x in nums:
                cur = max(0, cur + x)
                best = max(best, cur)
            return best

        total = sum(arr)
        if k == 1:
            return kadane(arr) % MOD

        best_two = kadane(arr * 2)
        if total > 0:
            return (best_two + (k - 2) * total) % MOD
        return best_two % MOD