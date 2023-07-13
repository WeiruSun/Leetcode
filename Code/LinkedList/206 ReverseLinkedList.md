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
Reverse the nodes two by two using three pointers. "next item" used to store the next node, "head" represent the current node, and "new head" represent the node before the head. 
For each loop, the code reverses the "head" and the "new head" and then passes the pointer to the next node separately.

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
Find the second last node need to be reversed (store in "head") and the last node (store in "head.next") 
let the last node point to the second last node and let the second last node point to None

```Java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while(curr != null){
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        return prev;
    }
}
```