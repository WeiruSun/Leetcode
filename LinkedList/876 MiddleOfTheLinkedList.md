# Middle of the Linked List

## Question description
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
### solution
```
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        
        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
        
        return slow
```
Use hare & tortoise algorithm.When the fast pointer hit the last node, the slow point is at the middle node.