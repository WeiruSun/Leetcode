# Reverse Nodes in k-Group

## Question description
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

### Iteratively
```
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        head = dummy
        while head != None:
            head = self.reverseNextK(head,k)
        return dummy.next
        
    def reverseNextK(self,head,k):
        nodeStart = head.next
        nodeK = head
        for i in range (k):
            nodeK = nodeK.next
            if nodeK == None:
                return nodeK
        
        nodeKPlus = nodeK.next
        newHead = None
        current = nodeStart
        
        while (current!= nodeKPlus):
            nextItem = current.next
            current.next = newHead
            newHead = current
            current = nextItem
        
        head.next = newHead
        nodeStart.next =  nodeKPlus
        
        return nodeStart
```
To reverse the linkedlist K by K, find the node after the K node and use it as condition to terminate the loop 


### Recursion
```
class Solution(object):
    def reverseKGroup(self, head, k):
        nkplus = head
        nstart = head
        for i in range(k):
            if nkplus == None:
                return nstart
            nkplus = nkplus.next

        newHead = self.reverse(nstart,nkplus)
        nstart.next = self.reverseKGroup(nkplus,k)
        return newHead
        
    
    def reverse(self, head, end):
        newHead = head
        while head!= end:
            nextItem = head.next
            head.next = newHead
            newHead = head
            head = nextItem
            
        return newHead
```     