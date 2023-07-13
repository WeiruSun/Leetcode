# question

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


solution 1: TLE
```
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i+1,i+k+1):
                if j > len(nums)-1:
                    continue
                if nums[i] == nums[j]:
                    return True
        return False
            
```
Solution 2: 
