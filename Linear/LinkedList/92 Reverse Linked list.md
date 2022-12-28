# Reversed Linked List II

## Question description
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
### Iteratively
```
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        guard = dummy
        for i in range(1,left):
            guard = guard.next
        
        current = guard.next
        
        for j in range(right-left):
            nextItem = current.next
            current.next = nextItem.next
            nextItem.next = guard.next
            guard.next = nextItem
        
        return dummy.next
```
The solution for iteration is to find the node before the left node then reverse the nodes two by two until encountering the right nodes
For reverse the nodes, using the head insertion method. Insert the node which after current node into the position after the guard node. 
Thus,"nextItem.next = guard.next" cannot be written as "nextItem.next = current" since 

### Recursion


