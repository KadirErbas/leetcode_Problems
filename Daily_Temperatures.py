#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
# O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) 
        myStack = [] # sıcaklık ve index ciftini saklar 
        
        for ix, temperature in enumerate(temperatures):
            while myStack and temperature > myStack[-1][0]:
                stackTemperature, stackIndex = myStack.pop()
                result[stackIndex] = (ix - stackIndex)
            myStack.append([temperature, ix])
        return result


'''
# O(n^2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        for i in range(len(temperatures)-1):
            counter = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    result[i] = counter
                    break
                else:
                    counter += 1      
        return result
'''

