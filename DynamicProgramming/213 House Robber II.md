# House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1 :
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
    

    def helper(self,nums):
        rob1, rob2 = 0,0
        for n in nums:
            # [1,2,3,4,5,6,1]
            newRob = max(rob1+n,rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

``` 




 ```
 class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        n = len(nums)
        v1 = self.helper(nums,0,n-2)
        v2 = self.helper(nums,1,n-1)
        return max(v1,v2)
    
    def helper(self,nums,start,end):
        if start == end:
            return nums[start]
        prevPrev = 0
        prev = nums[start]
        current = prev
        for i in range(start+1, end+1):
            current = max(prevPrev + nums[i], prev)
            prevPrev = prev
            prev = current
        return current
            
        
 
 
```

