# Binary Tree Postorder Traversal
Given the root of a binary tree, return the postorder traversal of its nodes' values.

```
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        res = []
        res = self.postorderHelper(root,res)
        return res
    
    def postorderHelper(self,root,res):
        if root is None:
            return None
        self.postorderHelper(root.left,res)
        self.postorderHelper(root.right,res)
        res.append(root.val)
        return res
        
```

