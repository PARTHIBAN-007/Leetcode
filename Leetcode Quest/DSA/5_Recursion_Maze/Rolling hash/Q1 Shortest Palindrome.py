"""
Shortest Palindrome

You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        concat = s + "#" + rev_s
        
        n = len(concat)
        kmp = [0] * n
        
        for i in range(1, n):
            j = kmp[i - 1]
            
            while j > 0 and concat[i] != concat[j]:
                j = kmp[j - 1]
            
            if concat[i] == concat[j]:
                j += 1
            
            kmp[i] = j
        
        palindrome_len = kmp[n - 1]
        prefix_to_add = s[palindrome_len:]
        return prefix_to_add[::-1] + s