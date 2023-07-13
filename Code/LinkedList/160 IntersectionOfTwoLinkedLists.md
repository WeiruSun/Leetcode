# Intersection of Two Linked Lists

## Question description
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:
The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

**Custom Judge:**

The inputs to the judge are given as follows (your program is not given these inputs):

* intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
* listA - The first linked list.
* listB - The second linked list.
* skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
* skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

### solution
```
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        
        for i in range(2):
            p1,p2 = self.findHead(p1,p2,headA,headB)
        
        while(p1 != p2):
                p1 = p1.next
                p2 = p2.next
        
        if p1 == None:
            return None
        else:
            return p1
        
    def findHead(self,p1,p2,headA,headB):
            while (p1!= None and p2!= None):
                p1 = p1.next
                p2 = p2.next
            
            if p1 == None:
                p1 = headB
            else:
                p2 = headA
            return p1,p2
```

use hare & tortoise algorithm. 
* someone's visualization of the solution : 
[Link to the visualization](https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!/165648)
