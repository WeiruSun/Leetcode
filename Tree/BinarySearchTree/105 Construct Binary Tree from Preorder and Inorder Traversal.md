# Construct Binary Tree from Preorder and Inorder Traversal
## Description
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

## solution1
```Python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        preorderLeft = []
        if index >0:
            preorderLeft = preorder[1:index+1]
            node.left =  self.buildTree(preorderLeft, inorder[:index])
        if index < len(inorder) -1:
            preorderright = preorder[len(preorderLeft)+1:]
            node.right = self.buildTree(preorderright, inorder[index+1:])
            
        return node
```

## solution精简版
```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:mid +1],inorder[:mid])
        node.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return node
```
