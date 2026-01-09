"""
Detect Capital

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals , small , chars = 0,0,0
        for char in word:
            o = ord(char)
            if o>=65 and o<=90:
                capitals+=1
            else:
                small +=1
            chars +=1
        if capitals==chars:
            return True
        if small == chars:
            return True
        first_is_cap = 65 <= ord(word[0]) <= 90 
        if first_is_cap and (small==chars-1):
            return True
        return False