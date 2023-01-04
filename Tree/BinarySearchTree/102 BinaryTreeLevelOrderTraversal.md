# Binary Tree Level Order Traversal

## Question description
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
### solution
```
from queue import Queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return None
        
        res = []
        q = Queue()
        q.put(root)
        
        while not q.empty():
            levelList = []
            levelSize = q.qsize()
            for i in range(levelSize):
                nodeN = q.get()
                levelList.append(nodeN.val)
                nodeL = nodeN.left
                nodeR = nodeN.right
                if nodeL !=None:
                    q.put(nodeL)
                if nodeR !=None:
                    q.put(nodeR)
            res.append(levelList)
        return res           
```