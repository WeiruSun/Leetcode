# Recover Binary Search Tree


## description
 ```
 class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if root is None:
            return
        # variable to store the value
        first = -1
        second = -1
        valueList = []
        self.inorderTraversal(root,valueList)
        
        for i in range(1,len(valueList)):
            if valueList[i-1].val < valueList[i].val:
                continue
                
            if first == -1 :
                first = i -1
            second = i
        
        temp = valueList[second].val
        valueList[second].val = valueList[first].val
        valueList[first].val = temp
        
    def inorderTraversal(self,root,valueList):
        if root == None:
            return
        
        self.inorderTraversal(root.left,valueList)
        valueList.append(root)
        self.inorderTraversal(root.right,valueList)
```

