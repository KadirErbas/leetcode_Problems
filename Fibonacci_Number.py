#!/usr/bin/env python
# coding: utf-8

# In[31]:


'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum of the two preceding ones, 
starting from 0 and 1.
'''
class Solution:
    def fib(self, n: int) -> int:
        if n <= 0 or n == 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
        
   
        '''        
        x = 0
        y = 0
        z = 1
        if n < 1:
            return 0
        while n > 1:
            x , y = y , z 
            n -= 1
            z = x + y            
        return z
        
        '''

