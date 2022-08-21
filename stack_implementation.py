#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:49:45 2022

@author: Amit Anchalia
"""

'''
Question:
    Implement stack (FILO/LIFO).

Notes:
    1. Insert
    2. Pop
    3. Peek
    4. isEmpty
    5. Length
    6. Create  

'''

class Stack(object):
    
    ## initialise the stack
    def __init__(self):
        self.items = []
     
    ## check if the stacks is empty
    def isEmpty(self):
        return self.items == []
    
    ## return top item in the stack
    def peek(self):
        return self.items[len(self.items)-1]
    
    ## insert the item passed as an arg
    def insert(self, item):
        self.items.append(item)
      
    ## remove and returns the item
    def pop(self):
        return self.items.pop()
    
    ## return the length of the stack
    def length(self):
        return len(self.items)
    
    ## displays the items in stack
    def display(self):
        print(self.items)
    
    
## Testing 

## Creating stack object 
stack = Stack()

## Checking if its empty
stack.isEmpty()

## Adding items
stack.insert(1)
stack.insert(2)
stack.insert(3)

## Peeking the items 
stack.peek()

## Removing the item
stack.pop()

## Peeking the items 
stack.peek()

## Check the length of the stack
stack.length()

## Display stack
stack.display()