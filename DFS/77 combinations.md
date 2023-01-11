# Combination Sum

## Question description
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
 ### solution
```
class Solution:
    res = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        currentList = []
        self.helper(n, k, currentList,1)
        return self.res
    
    
    def helper(self, n, k, currentList,start):
        if len(currentList)== k:
            self.res.append(currentList.copy())
            return
        
        for i in range(start,n+1):
            currentList.append(i)
            self.helper(n,k,currentList,i+1)
            currentList.pop(len(currentList)-1)

```

the length of the result list is limited to k. And this is the end condition of dfs. 
