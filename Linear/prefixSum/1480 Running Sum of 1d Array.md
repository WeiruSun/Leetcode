# question

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

```
 prefixSum = []
        current = 0

        for i in range(len(nums)):
            current += nums[i]
            prefixSum.append(current)
        return prefixSum
```

