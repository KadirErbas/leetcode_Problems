#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
'''
class MyStack:

    def __init__(self):
        self.myQueue = deque()

    def push(self, x: int) -> None:
        self.myQueue.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.myQueue)-1):
            self.myQueue.append(self.myQueue.popleft())
        return self.myQueue.popleft()

    def top(self) -> int:
        return self.myQueue[-1]

    def empty(self) -> bool:
        return len(self.myQueue) == 0


# In[ ]:




