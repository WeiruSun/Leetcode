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
        if len(nums) == 0 or nums is None:
            return -1
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
        
        left = 1
        right = len(nums)-1
        while left < right:
            mid = (right - left)//2 + left
            print("mid", mid)
            if nums[mid]> nums[mid-1] and nums[mid + 1] < nums[mid]:
                return mid
            elif nums[mid-1]< nums[mid]<nums[mid+1]:
                left = mid +1
                print("left",left)
            else:
                right = mid 
                print("right",right)
        return -1
        
        
```