# Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.
 ```
 class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        
        res = []
        res = self.preorderhelper(root,res)
        return res
    
    def preorderhelper(self,root,res):
        if root is None:
            return None
        res.append(root.val)
        self.preorderhelper(root.left,res)
        self.preorderhelper(root.right,res)
        return res
```

