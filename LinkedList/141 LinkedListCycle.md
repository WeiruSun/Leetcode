# Linked List Cycle

## Question description
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
### solution
```
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        slow = head
        fast = head
        
        while(fast != None and fast.next!= None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False
```

Use hare & tortoise algorithm. The fast pointer and slow point would meet at one node if there is circle in the linked list