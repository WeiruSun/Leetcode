# Binary Tree Level Order Traversal II

## Question description
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
### solution
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return None
        
        q = Queue()
        q.put(root)
        
        res = []
        while not q.empty():
            levelSize = q.qsize()
            levelList = []
            for i in range(levelSize):
                nodeN = q.get()
                levelList.append(nodeN.val)
                nodeL = nodeN.left
                nodeR = nodeN.right
                if nodeL != None:
                    q.put(nodeL)
                if nodeR != None:
                    q.put(nodeR)
            
            res.append(levelList)
            
            
        return res[:: -1]

            

```
