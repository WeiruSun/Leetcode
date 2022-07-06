# Find Peak Element

## Question description
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

### solution
```
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
        
        left = 1
        right = len(nums)-2
        while left <= right:
            mid = (right - left)//2 + left
            if nums[mid -1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid -1] > nums[mid]:
                right = mid -1
            else:
                left = mid + 1
        
        return None
        
        
```