# Remove Duplicates from Sorted List

## Question description
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


### solution
```
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        slow = head
        fast = head
        
        if head is None:
            return None
        
        while(fast != None):
            if fast.val == slow.val:
                fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
        
        slow.next = None
        return dummy.next
```

use hare & tortoise algorithm. compare the value of fast pointer and the slow point and let fast point move forward until the fast pointer point to a different value. 
Notice the test case could be [ ] or [0,0,0,0,]