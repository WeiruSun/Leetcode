# Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 ```
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current and current.next:
            nextItem = current
            nextNextItem = current.next
            
            prev.next = nextNextItem
            nextItem.next = nextNextItem.next
            nextNextItem.next = nextItem
            
            prev = nextItem
            current = nextItem.next
           
           
        return dummy.next
            
                
                
        
```

