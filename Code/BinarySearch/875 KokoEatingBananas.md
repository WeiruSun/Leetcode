# Koko Eating Bananas

## Question description
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

### solution
```
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        left = 0
        right = max(piles)
        
        while (left <= right):
            k = (right - left)//2 + left
            if k == 0:
                return 1
            hours = self.findHours(piles, k)
            if hours > h:
                left = k + 1
            else:
                right = k -1
        return left
    
    
    def findHours(self,piles, k):
        hours = 0
        for i in piles:
            hours += i//k
            if i % k != 0:
                hours += 1
        return hours
            
```
The hours to finish the bananas is increasing order
* corner case 1 : [312884470] 968709470