# Combination Sum III


Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

```
class Solution:
    res = []
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        currentList = []
        self.helper(k,n,1,currentList)
        return self.res
    
    def helper(self,k,target,start,currentList):
        if len(currentList) == k and target == 0:
            self.res.append(currentList.copy())
            return
        for i in range(start,10):
            if i > target:
                return
            currentList.append(i)
            self.helper(k,target - i,i+1,currentList)
            currentList.pop()
```

