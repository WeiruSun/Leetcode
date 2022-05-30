# Binary Search

## Question description
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

### solution
```
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        
        while (left <= right):
            mid = (right-left)//2 + left
            if nums[mid]== target:
                return mid
            if nums[mid]< target:
                left = mid +1
            else: 
                right = mid-1
        return -1
```

note: 
* mid = (right-left)//2 + left    
   avoid the out of index problem
* (left <= right)
    the condition for quitting the loop is left > right 