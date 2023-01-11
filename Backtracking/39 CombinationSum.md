# Combination Sum

## Question description
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

```python
Input: candidates = [2,3,6,7], target = 7

Output: [[2,2,3],[7]]

Explanation:

2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

 ### solution
可重复
```
class Solution:
    res = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        currentList = []
        candidates.sort()
        self.helper(candidates,target,0,currentList)
        return self.res
    
        
    
    def helper(self,candidates, target, start,currentList):
        if target == 0:
            self.res.append(currentList.copy())
            return
        for i in range(start,len(candidates)):
            if candidates[i] > target:
                return
            currentList.append(candidates[i])
            self.helper(candidates, target-candidates[i], i,currentList)
            currentList.pop(len(currentList)-1)
           
```