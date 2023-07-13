# Range Sum Query - Immutable

## Question description
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

**solution1 - 暴力解法**

直接遍历left到right的index进行求和

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right+1):
            sum += self.nums[i]
        return sum
```

每次调用平均需要O(n)时间

**Solution2 - 前缀和解法** 

空间换时间，对nums进行预处理，用数组preSum[i]表示前i个元素的和

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = [0]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.preSum.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1] -self.preSum[left]
```

查询时间为O（1）