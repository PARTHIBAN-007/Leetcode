"""
 Longest Word in Dictionary

Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.
Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

 

Example 1:
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters. 
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False
        self.character = ''

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self._insert(word)
        return self._dfs(self.root, "")

    def _insert(self, word: str) -> None:
        node = self.root
        for c in word:
            i = ord(c) - 97
            if node.children[i] is None:
                node.children[i] = TrieNode()
                node.children[i].character = c
            node = node.children[i]
        node.is_end_of_word = True

    def _dfs(self, node: TrieNode, path: str) -> str:
        res = path
        for child in node.children:
            if child and child.is_end_of_word:
                s = self._dfs(child, path + child.character)
                if len(s) > len(res) or (len(s) == len(res) and s < res):
                    res = s
        return res
