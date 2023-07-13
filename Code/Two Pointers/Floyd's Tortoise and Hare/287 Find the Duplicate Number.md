# Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space

Consideration:

Given n

len(integer array): n+1

integer range: [1, n]

## solution using dict 
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) -1
        count_dic = {}
        count_dic = {i: 0 for i in range(1,n+1)}
        for i in range(0,len(nums)):
            number = nums[i]
            count_dic[number] +=1
            if count_dic[number] ==2:
                return number
 
```

##solution using linked list

```python


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        slow = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if slow == fast:
                break

        return slow

```