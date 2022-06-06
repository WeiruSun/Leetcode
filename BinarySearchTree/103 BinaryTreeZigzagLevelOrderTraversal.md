# Binary Tree Zigzag Level Order Traversal

## Question description
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
### solution
```
from queue import Queue
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return None
        
        q = Queue()
        q.put(root)
        res = []
        counter = 0
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
            counter +=1
            if counter %2 ==0:        
                levelList.reverse()
            print(levelList)
            res.append(levelList)
        return res
```