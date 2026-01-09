"""
Sum of Square Numbers

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 

Constraints:

0 <= c <= 231 - 1
"""
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.isqrt(c))  

        while l <= r:
            current = l * l + r * r
            if current == c:
                return True
            elif current < c:
                l += 1
            else:
                r -= 1

        return False