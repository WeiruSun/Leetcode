# Traversal of binary tree

# Preorder
```
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preorderHelper(root,res)
        return res

    def preorderHelper(self,root,res):
        if root:
            res.append(root.val)
            self.preorderHelper(root.left,res)
            self.preorderHelper(root.right,res)
```

# Inorder

![img.png](inorderTraversal.png)
```
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inOrderHelper(root,res)
        return res
    
    def inOrderHelper(self,root,res):
        if root:
            self.inOrderHelper(root.left,res)
            res.append(root.val)
            self.inOrderHelper(root.right,res)
```

# postorder

```
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postorderHelper(root,res)
        return res
    
    def postorderHelper(self,root,res):
        if root :
            self.postorderHelper(root.left,res)
            self.postorderHelper(root.right,res)
            res.append(root.val)
```
