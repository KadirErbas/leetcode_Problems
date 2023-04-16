#!/usr/bin/env python
# coding: utf-8

# In[70]:


'''
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.
'''

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        myStack = []
        for opr in operations:        
            if opr == "C":
                myStack.pop()
            
            elif opr == "D":
                myStack.append(int(myStack[len(myStack)-1]) * 2)
                        
            elif opr == "+":
                myStack.append(int(myStack[len(myStack)-1]) + int(myStack[len(myStack)-2]))  
            
            else:
                myStack.append(int(opr))

        return sum(myStack)


# In[71]:


solution()

