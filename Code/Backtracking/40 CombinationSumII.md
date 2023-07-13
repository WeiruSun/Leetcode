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
        candidates.sort()
        currentList = []
        self.backtracking(candidates, target, 0, currentList)
        return self.res
    
    def backtracking(self,candidates,target,start,currentList):
        if target == 0:
            self.res.append(currentList.copy())
            return
        
        i = start
        while i < len(candidates):
            if candidates[i] > target:
                return
            currentList.append(candidates[i])
            self.backtracking(candidates,target-candidates[i],i+1,currentList)
            currentList.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i +=1
            i+=1 
```