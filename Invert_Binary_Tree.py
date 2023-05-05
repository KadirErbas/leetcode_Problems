#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #Exit condition
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left # Replace
        
        #Recursive
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

