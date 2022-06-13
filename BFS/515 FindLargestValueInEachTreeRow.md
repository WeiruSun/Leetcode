# Find Largest Value in Each Tree Row

## Question description
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
### solution
```
from queue import Queue
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return None
        
        q= Queue()
        q.put(root)
        output = []
        
        while not q.empty():
            size = q.qsize()
            levelList = []
            for i in range(size):
                nodeN = q.get()
                levelList.append(nodeN.val)
                nodeL = nodeN.left
                nodeR = nodeN.right
                if nodeL !=None:
                    q.put(nodeL)
                if nodeR !=None:
                    q.put(nodeR)
            largest = max(levelList)
            output.append(largest)
        
        return output
```