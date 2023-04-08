# Merge Two Sorted Lists

## Question description
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### solution
```
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        p1 = list1
        p2 = list2
        cur = dummy
        while (p1 != None and p2 != None):
            if p1.val > p2.val:
                cur.next = p2
                p2 = p2.next
            else:
                cur.next = p1
                p1 = p1.next
            cur = cur.next
        if p1 != None:
            cur.next = p1
        if p2 != None:
            cur.next = p2;
        
        return dummy.next
```
create three pointer for list1, list2 and the result list, compare the node's value and let the result list's pointer point to the smaller node

```Java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode newHead = dummy;

        ListNode p1 = list1;
        ListNode p2 = list2;

        while(p1 != null && p2 != null){
            if(p1.val > p2.val){
                newHead.next = p2;
                p2 = p2.next;
            }
            else{
                newHead.next = p1;
                p1 = p1.next;
            }
            newHead = newHead.next;
        }

        if(p1 == null){
            newHead.next = p2;
        }
        if(p2 == null){
            newHead.next = p1;
        }

        return dummy.next;
    }
}
```