# House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## solution
rob = max(arr[0]+rob[2:n],arr[1:n])

time complexity : O(n)
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0 ,0

        #[rob1,rob2,n,n+1]
        # store the max value we can rob up until this point
        for n in nums:
            temp = max(n+rob1,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
```
```Python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))
        for i in range(2,n):
            dp.append(max(nums[i] + dp[i-2],dp[i-1]))
        
        return dp[n-1]
        
```

```Python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        prevPrev = 0
        prev = nums[0]
        current = prev
        for i in range(1,n):
            current = max(prevPrev + nums[i],prev)
            prevPrev = prev
            prev = current
            
        return current
    
```

robFrom(i)=max(robFrom(i+1),robFrom(i+2)+nums(i))



