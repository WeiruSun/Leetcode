# Permutations

## Question description
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 ### solution
```
class Solution:
    res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        currentList = []
        self.backtracking(nums,currentList)
        return self.res

    def backtracking(self,nums,currentList):
        if len(currentList) == len(nums):
            self.res.append(currentList.copy())
            return
        for i in range(len(nums)):
            if nums[i] not in currentList:
                currentList.append(nums[i])
                self.backtracking(nums,currentList)
                currentList.pop()
```
the result list is permutations, not combinations, so we do not need a label for the start point in the dfs
To avoid the repetition of the elements, we need to check if the current element is already in the currentList


