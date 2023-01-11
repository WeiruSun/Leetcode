# Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.
```
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        res = []
        res = self.inOrderHelper(root,res)
        return res
    
    def inOrderHelper(self,root,res):
        if root is None:
            return None
        
        self.inOrderHelper(root.left,res)
        res.append(root.val)
        self.inOrderHelper(root.right,res)
        return res
```

