#!/usr/bin/env python
# coding: utf-8

# In[74]:


'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
'''
# Floyd's Algorithm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowPointer = 0
        fastPointer = 0
        while True:
            print (f"slow = {slowPointer}, fast = {fastPointer}")
            slowPointer = nums[slowPointer]
            fastPointer = nums[nums[fastPointer]]
            if slowPointer == fastPointer:
                print (f"slow = {slowPointer}, fast = {fastPointer}")           
                break
        secondSlowPointer=0
        print("----"*5)
        while True:
            print (f"slow = {slowPointer}, slow2 = {secondSlowPointer}")
            slowPointer = nums[slowPointer]
            secondSlowPointer = nums[secondSlowPointer]
            if slowPointer == secondSlowPointer:
                print (f"slow = {slowPointer}, slow2 = {secondSlowPointer}")            
                return slowPointer


# In[ ]:


'''
        O(n^2)
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return nums[i]
'''

