# Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = -1001
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.res
    
    def helper(self,root):
        if root is None:
            return 0
        left = max(self.helper(root.left),0)
        right = max(self.helper(root.right),0)
        sumValue = root.val + left + right
        self.res = max(self.res,sumValue)
        return max(left + root.val, right + root.val)
        


```

