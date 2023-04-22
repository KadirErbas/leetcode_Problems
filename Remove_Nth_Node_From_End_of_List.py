#!/usr/bin/env python
# coding: utf-8

# In[186]:


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leftPointer = head
        rightPointer = head

        while rightPointer and n > 0:
            rightPointer= rightPointer.next
            n -= 1
        
        while rightPointer and rightPointer.next:
            leftPointer = leftPointer.next
            rightPointer= rightPointer.next
        
        if leftPointer == head and not rightPointer:
            return head.next
        
        leftPointer.next= leftPointer.next.next

        return head

''' 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        leftPointer = head
        rightPointer = head
        sayac = 0

        while rightPointer.next:
            rightPointer = rightPointer.next
            sayac += 1
        
        if sayac == 0:
            return
        
        elif sayac == 1:
            if n == 1:
                leftPointer.next = None
                return head
            elif n == 2:              
                return head.next    
        
        sayac2 = sayac - n
        if sayac2 < 0:
            return head.next
        
        while sayac2 > 0:
            leftPointer = leftPointer.next
            sayac2 -= 1
        
        leftPointer.next = leftPointer.next.next      
        return head

'''

