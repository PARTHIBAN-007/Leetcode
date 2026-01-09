"""
K-th Smallest in Lexicographical Order

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:
Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

Example 2:
Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 109

"""

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        i = 1
        def count(cur):
            res = 0
            nei = cur +1
            while cur <=n:
                res += min(nei,n+1) -cur
                cur *=10
                nei *=10
            return res


        while i <k:
            steps = count(cur) 
            if i+steps<=k:
                cur +=1
                i+=steps

            else:
                cur*=10
                i+=1
        return cur                   