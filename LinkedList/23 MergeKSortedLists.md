# Merge k Sorted Lists

## Question description
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


### solution
```
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        head = dummy
        heap = PriorityQueue()
        
        for i in lists:
            if i:
                heap.put((i.val,i))
            
        while not heap.empty():
            value,node = heap.get() 
            head.next = ListNode(value)
            head = head.next
            node = node.next
            if node:
                heap.put((node.val,node))
        return dummy.next
            
```


The idea is similar to the problem 21 "Merge two sorted lists", but use heap to store the nodes' values and nodes from lists, pop the smallest element in heap, let head point to this element, and put the node after this node into heap

Note:

**Python heapq**
* heapq.heappush(heap, item)

* heapq.heappop(heap)
  (To access the smallest item without popping it, use heap[0].)
* heapq.heappushpop(heap, item)
* heapq.heapify(x): 
Transform list x into a heap, in-place, in linear time.
* heapq.heapreplace(heap, item)

**Priority Queue**
* pQueue.put(value)
* pQueue.get()