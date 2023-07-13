# Heap

track the smallest object in the list, and remove it when needed

## use list
Continually sort the list and remove the smallest element. 

Sorting takes O(nlogn)
```Python
arr = [4,6,7,1]
new = [[1], [], [9,9], [5]]
for ne in new:
  arr.append(ne)
  arr.sort()
  print(arr)
  del arr[0]
```

## use heapq
heapq is used to maintain fast popping of the smallest element, the baseline method of iterating through the whole array for the for the smallest element will take O(n) time

```python
arr = [4,6,7,1]
import heapq
heapq.heapify(arr)
print(arr) # [1, 4, 7, 6]

heapq.heappush(arr,4) # push an element
popped = heapq.heappop(arr) # returns the smallest element
```
