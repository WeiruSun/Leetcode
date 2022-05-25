# Reversed Linked List

## Question description

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Solution

### Iteratively

```
class Solution(object):
    def reverseList(self, head):
    newhead = None
    while head != None:
        nextItem = head.next
        head.next = newhead
        newhead = head
        head = nextItem
    return newhead

```

### Recursion

```
class Solution(object):
    def reverseList(self, head):
        if (head == None or head.next == None):
            return head
        
        last = self.reverseList(head.next)
     
        head.next.next = head
        head.next = None
        
        return last
```



