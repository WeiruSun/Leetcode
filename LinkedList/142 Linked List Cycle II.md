# Linked List Cycle II


Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.


## Note
data structure: linked list

after k steps, two pointers meet. 

assume the length of cycle is r

2k - k = nr

assume the length between the head and the start node of cycle is s

the distance between the start node of cycle and the first meeting node is m

s = k - m = nr - m 

 ```
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        fast = head
        slow = head
        isCycle = False
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                isCycle = True
                break
        if not isCycle:
            return None
        else:
            slow = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
        
        return slow
        
        
```

