"""
Longest Happy Prefix

A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).
Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

 

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
Example 2:

Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.

"""

class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0]*n

        j = 0
        for i in range(1,n):
            while j>0 and s[i]!=s[j]:
                j = lps[j-1]
            if s[i]==s[j]:
                j+=1
            lps[i] = j
        return s[:lps[n-1]]