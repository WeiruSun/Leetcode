# Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while p1 is not None or p2 is not None or carry != 0:
            if p1 is not None :
                value1 = p1.val
            else:
                value1 = 0
            if p2 is not None:
                value2 = p2.val
            else:
                value2 = 0
                
            currentValue = value1 + value2 + carry
            carry = currentValue //10
            current.next = ListNode(currentValue % 10)
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            current = current.next
        return dummy.next
            
    
        
```

