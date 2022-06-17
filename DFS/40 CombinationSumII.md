# Combination Sum II

## Question description
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 ### solution
```
class Solution:
    res = []
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        currentList = []
        candidates.sort()
        self.helper(candidates,target,currentList,0)
        return self.res
    
    
    def helper(self, candidates, target, currentList,start):
        if target == 0:
            self.res.append(currentList.copy())
            return
        i = start
        while i < len(candidates):
            if candidates[i] > target:
                return
            currentList.append(candidates[i])
            self.helper(candidates, target-candidates[i], currentList,i+1)
            currentList.pop(len(currentList)-1)
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            i+=1
            
```