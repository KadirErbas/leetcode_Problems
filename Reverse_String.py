#!/usr/bin/env python
# coding: utf-8

# In[31]:


'''
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
'''


# In[28]:


class Solution:
    def reverseString(self, s: List[str]) -> None: 
        """
        Do not return anything, modify s in-place instead.
        """        
        leftIndex = 0
        rightIndex = len(s)-1
        while leftIndex < rightIndex:
            s[leftIndex] , s[rightIndex] = s[rightIndex] , s[leftIndex]        
            rightIndex -= 1
            leftIndex += 1     
        
        '''
        # listenin tersini listenin başına ekleme
        for i in range(0,len(s)*2,2):
            s.insert(0,s[i])
        
        # listenin ters çevrilmemiş elemanları silme
        for i in range(int(len(s)/2)):
            s.pop()
        '''
        # s.reverse()

