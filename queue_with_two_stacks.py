#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 16:13:44 2022

@author: Amit Anchalia
"""

'''
Question:
    Given the Stack class below, implement a Queue class using two stacks! 
    
    Note, this is a "classic" interview problem. Use a Python list data structure as your Stack.
'''

# class Stack(object):
    
#     ## initialise the stack
#     def __init__(self):
#         self.items = []
     
#     ## check if the stacks is empty
#     def isEmpty(self):
#         return self.items == []
    
#     ## return top item in the stack
#     def peek(self):
#         return self.items[len(self.items)-1]
    
#     ## insert the item passed as an arg
#     def insert(self, item):
#         self.items.append(item)
      
#     ## remove and returns the item
#     def pop(self):
#         return self.items.pop()
    
#     ## return the length of the stack
#     def length(self):
#         return len(self.items)
    
#     ## displays the items in stack
#     def display(self):
#         print(self.items)
        
class Queue2Stacks():
    
    ## initialise the stack
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        

    def enqueue(self, item):
        self.stack_1.append(item)
        
    def dequeue_m1(self):
        
        ## Reverse the order by popping from stack 1 to 2
        stack_1_len = len(self.stack_1)
        for i in range(stack_1_len):
            popped_item = self.stack_1.pop()
            
            ## Break before the last element to be dequeued
            if (i == (stack_1_len-1)):
                break
            
            self.stack_2.append(popped_item)
         
        ## re-inserting the value back to stack 1
        stack_2_len = len(self.stack_2)
        for i in range(stack_2_len):
            self.stack_1.append(self.stack_2.pop())
        
        return popped_item
    
    
    def dequeue_m2(self):
        
        ## Check if stack 2 is empty
        if not self.stack_2:
            ## if stack 1 is not empty pop out all the items and append to stack 2
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        
        ## Return the top of stack 2 which was bottom of stack 1
        return self.stack_2.pop()
            
            
  
## Testing
q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print(q.dequeue_m2())