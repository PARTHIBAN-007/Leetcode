"""
Maximum Prime Difference

You are given an integer array nums.
Return an integer that is the maximum distance between the indices of two (not necessarily different) prime numbers in nums.

 

Example 1:
Input: nums = [4,2,9,5,3]
Output: 3
Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.

Example 2:
Input: nums = [4,8,2,8]
Output: 0
Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.

 

Constraints:

1 <= nums.length <= 3 * 105
1 <= nums[i] <= 100
The input is generated such that the number of prime numbers in the nums is at least one.
"""
from typing import List
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        first = last = -1

        for i, num in enumerate(nums):
            if is_prime(num):
                first = i
                break
        last = i
        for i in range(len(nums) - 1, -1, -1):
            if is_prime(nums[i]):
                last = i
                break
        print(first,last)
        return last - first