# Remove Nth Node From End of List

## Question description
Given the head of a linked list, remove the nth node from the end of the list and return its head.

### solution
```
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
    
        fast = head
        slow = dummy
        for i in range(n):
            fast = fast.next
                
        while (fast != None):
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next
```

use hare & tortoise algorithm. let the fast point k nodes away from slow pointer, then the slow pointer is the node before the N node 