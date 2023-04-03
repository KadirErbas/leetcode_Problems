#!/usr/bin/env python
# coding: utf-8

# In[8]:


"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

"""  
    
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        result = 0 
        
        for number in nums:
            result = number ^ result # xor with number
        
        return result
        
        """
        nums listesinin içindeki numaraları; set'te o eleman yoksa set'in içine atar, varsa o elemanı set'ten çıkarır. 
        Sonra set'in içindeki yalnız kalan elemanları yazdırır.
        
        mySet = set()        
        for num in nums:
            if num in mySet:
                mySet.remove(num)
            else:
                mySet.add(num)       
        for i in mySet:
            return i
        """

