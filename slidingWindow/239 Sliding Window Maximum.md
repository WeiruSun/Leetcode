# Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.


## note
数据结构： 
q = deque()
res = []
遍历nums:
1. 当 i < k-1 时:

   将当前数（nums[i]）加入q
2. 当 i >= k-1时（已到第一个窗最后一个数）

      A. 将当前数（nums[i]）加入q

      B. 找出q中最大值
        
      C. 如果当前窗起始位置上的数（nums[i-k+1]）为q中最大值，则pop这个值，以避免影响判断


```
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(len(nums)):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            #print(q)
            if q and i >= k -1:
                res.append(q[0])
                if nums[i-k+1] == q[0]:
                    q.popleft()
        return res
            
```

```
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        for i in range(len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if q[0] == i-k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
```

