"""
Construct Binary Tree from Inorder and Postorder Traversal
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.

"""
from typing import Optional
class TreeNode:
    pass

from typing import List
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indices = {v: i for i, v in enumerate(inorder)}
        self.pro_idx = len(postorder)-1
        def dfs(l, r):
            if l > r:
                return None

            root = TreeNode(postorder[self.pro_idx])
            self.pro_idx -=1
            idx = indices[root.val]
            root.right = dfs(idx + 1, r)
            root.left = dfs(l, idx - 1)
            return root

        return dfs(0, len(inorder) - 1)