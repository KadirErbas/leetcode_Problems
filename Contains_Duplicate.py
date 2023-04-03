#!/usr/bin/env python
# coding: utf-8

# In[8]:


"""
Contains Duplicate
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.

"""  
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myHashSet = set()        # bos set oluşturur
        for num in nums:         # nums listesindeki numaraları her döngüde teker teker num değişkenine atar
            if num in myHashSet: # myHashSet imizde num değişkenimizin bulunup bulunmadığını kontrol eder. koşul doğruysa True donderir.
                return True
            myHashSet.add(num)   # myHashSet imize bu numarayı ekler.
        return False


# In[ ]:





# In[ ]:




