# Kth Missing Positive Number

## Question description
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.
### solution
```
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        left = 0
        right = len(arr)-1
        
        while (left <= right):
            mid = (right-left)//2 + left
            mid_missing_number = self.findMissingNumber(arr,mid)
            if mid_missing_number < k:
                left = mid +1
            if mid_missing_number >= k:
                right = mid -1
                
        return arr[right]+k - self.findMissingNumber(arr,right)
            
    def findMissingNumber(self,arr,x):
        # x as index
            return arr[x]-1-x

```

input :[2,3,4,7,11] k = 5
left = 0, right = 4

1. mid = 2, list[2] = 4, missing number = 4 - 2 -1 = 1 < k = 5
let left = mid +1 = 3
2. mid = (left + right)//2 = 3, list[3] = 7, missing number = 7 - 3 - 1 = 3 <k = 5
let left = mid + 1 = 4
3. mid = (left + right)//2 = 4, list [4] = 11, missing number = 11 - 4 - 1 = 6 >k = 5
let right = mid -1 = 3
4. since left > right, quit the loop. 
now we can calculate the kth missing value = k - findMissingNumber(arr,right) + arr[right]:




