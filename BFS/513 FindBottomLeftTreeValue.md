# Find Bottom Left Tree Value
## Question description
Given the root of a binary tree, return the leftmost value in the last row of the tree.
### solution
```
from queue import Queue
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        q = Queue()
        q.put(root)
        left = 0
        while not q.empty():
            size = q.qsize()
            
            for i in range(size):
                nodeN = q.get()
                left = nodeN.val
                nodeL = nodeN.left
                nodeR = nodeN.right
                if nodeR is not None:
                    q.put(nodeR)
                if nodeL is not None:
                    q.put(nodeL)
        
        return left
                    
```