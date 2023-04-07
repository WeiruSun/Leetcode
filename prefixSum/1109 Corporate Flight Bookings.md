# Corporate Flight Bookings


## Question description
There are n flights that are labeled from 1 to n.

You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

###solution
```
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = []
        for i in range(n):
            diff.append(0)
        for item in bookings:
            start = item[0]-1
            end = item[1]-1
            difference = item[2]
            diff[start] += difference
            if end +1 < n:
                diff[end+1] -= difference
                
        for i in range(1,n):
            diff[i] += diff[i-1]
            
        return diff

```

