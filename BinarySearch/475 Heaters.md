# Heaters

## Question description
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.
### solution
```
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        heaters.sort()
        res = 0
        for i in range(len(houses)):
            cur_distance = 0
            left_heater_index = self.findHeater(heaters,houses[i])
            right_heater_index = left_heater_index + 1
            left_distance = 0
            right_disntace = 0
            if(left_heater_index < 0):
              # if there is not left heater
                left_distance = -1
            else:
                # get left distance
                left_distance = houses[i]-heaters[left_heater_index]
            if(right_heater_index >= len(heaters)):
                # if there is no right heater
                right_distance = -1
            else:
                # get right distance
                right_distance = heaters[right_heater_index]-houses[i]
            if(left_distance == -1):
                cur = right_distance
            elif right_distance == -1:
                cur = left_distance
            else:
                cur = min(left_distance,right_distance)
            res = max(cur,res)
            
        return res
    
    def findHeater(self,heaters, house_index):
        left = 0
        right = len(heaters)-1
        while (left <= right):
            mid = (right-left)//2 + left
            heater_index = heaters[mid]
            # we want to find the left boundary
            if heater_index < house_index:
                left = mid + 1
            if heater_index >= house_index:
                right = mid -1
            # we find the last heater that is on the left of current house
        return right

```