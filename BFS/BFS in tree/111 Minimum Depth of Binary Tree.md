# Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 ```
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 1
        if root is None:
            return 0
        q = Queue()
        q.put(root)
        while not q.empty():
            levelSize = q.qsize()
            for i in range(levelSize):
                nodeN = q.get()
                if nodeN.left is None and nodeN.right is None:
                    return depth
                if nodeN.left is not None:
                    q.put(nodeN.left)
                if nodeN.right is not None:
                    q.put(nodeN.right)
            depth += 1
                
        return 0
```

