"""
Target Sum

You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

"""

from typing import List
class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        total = sum(arr)

        if (total + target) % 2 != 0 or (total + target) < 0:
            return 0
        
        tar = (total + target) // 2
        n = len(arr)

        dp = [[0] * (tar + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for t in range(0, tar + 1):
                
                dp[i][t] = dp[i - 1][t]
                if arr[i - 1] <= t:
                    dp[i][t] += dp[i - 1][t - arr[i - 1]]

        return dp[n][tar]
