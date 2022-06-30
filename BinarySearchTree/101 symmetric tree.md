# Symmetric Tree

## description

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
```
 class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkSymmetric(root,root)
        
        
    def checkSymmetric(self,left,right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            return self.checkSymmetric(left.left,right.right) and self.checkSymmetric(right.left,left.right) and left.val == right.val
```

