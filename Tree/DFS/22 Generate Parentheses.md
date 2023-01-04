# Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 ```
 class Solution:
    res = []
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return[]
        self.res = []
        currentList = []
        self.helper(n,currentList,0,0)
        return self.res
    
    def helper(self,n,currentList,openCount,closeCount):
        if openCount == n and closeCount == n:
            self.res.append("".join(currentList.copy()))
        
        if openCount < n:
            currentList.append("(")
            self.helper(n,currentList,openCount+1,closeCount)
            currentList.pop()
        
        if closeCount < openCount:
            currentList.append(")")
            self.helper(n,currentList,openCount,closeCount+1)
            currentList.pop()
        
    
```

