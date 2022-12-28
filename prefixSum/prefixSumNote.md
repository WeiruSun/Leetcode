# prefix sum
## definition
前缀和指一个数组的某下标之前的所有数组元素的和（包含其自身）。 前缀和分为一维前缀和，以及二维前缀和。 前缀和是一种重要的预处理，能够降低算法的时间复杂度

## 实现 
### leetcode 1480 Running Sum of 1d Array
```
prefixSum = []
current = 0
for i in range(len(nums):
    current += nums[i]
    prefixSum.append(current)

```

## 例题 
### 724 Find Pivot index
```
Input: nums = [1,7,3,6,5,6]

prefixSum = [1,8,11,17,22,28]
```
判断条件为：left = right
```
left = prefixSum[i] - nums[i]
right = prefixSum[len(prefixSum)-1]-prefixSum[i]
```