#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

"""  

class Solution:
    def majorityElement(self, nums: List[int]) -> int:            
        numbers = {}
        maxValue = 0
        result = 0

        for i in nums:
            numbers[i] = numbers.get(i,0) + 1
            if maxValue < numbers[i]:
                maxValue = numbers[i]
                result = i
        return result


# In[ ]:




