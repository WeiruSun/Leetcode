# permutation II

## Question description
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 ### solution
```
class Solution:
    res = []
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        currentList = []
        nums.sort()
        used = []
        for i in range(len(nums)):
            used.append(False)
        self.helper(nums,currentList,used)
        return self.res
    
    def helper(self, nums, currentList,used):
        if len(currentList) == len(nums):
            self.res.append(currentList.copy())
            return
        i = 0
        while i < len(nums):
            if used[i]:
                i += 1
                continue
            else:
                currentList.append(nums[i])
                used[i] = True
                self.helper(nums,currentList,used)
                currentList.pop()
                used[i] = False
                while i+1 < len(nums) and nums[i]==nums[i+1]:
                    i += 1
                i += 1
                
```

cannot reuse the element, give the permutation in all order. this indicates that there is no need to use start label to tell the recursion where to start iterating. 
but to ensure we do not use element repetitively, we need to label each number in the nums to see if we have put the element in the current List