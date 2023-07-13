# Search Insert Position

## Question description
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
### solution
```
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums)-1
        
        while (left <= right):
            mid = (right - left)//2 + left
            
            if nums[mid] == target:
                return mid
            if nums[mid]< target:
                left = mid +1
            else:
                right = mid -1
        
        return left
    
```
The question is similar to the problem 704
the return value is left because when the loop terminated, left pointer is on the right side of right pointer