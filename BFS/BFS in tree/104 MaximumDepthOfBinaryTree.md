# Maximum Depth of Binary Tree

## description
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
```
 from queue import Queue
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        counter = 0
        if root is None:
            return counter
        if root.left == None and root.right == None:
            return 1
        q = Queue()
        q.put(root)
        
        while not q.empty():
            levelSize = q.qsize()
            for i in range(levelSize):
                node = q.get()
                nodeL = node.left
                nodeR = node.right
                if nodeL is not None:
                    q.put(nodeL)
                if nodeR is not None:
                    q.put(nodeR)
            counter += 1
            print("counter",counter)
        return counter
```

