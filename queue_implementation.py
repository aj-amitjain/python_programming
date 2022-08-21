#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 12:02:17 2022

@author: Amit Anchalia
"""

'''
Question:
    Implement queue (FIFO).

Notes:
    1. Enqueue (Insert)
    2. Dequeue (Pop)
    3. isEmpty
    4. Length
    5. Create  

'''

class Queue(object):
    
    ## initialise the stack
    def __init__(self):
        self.items = []
     
    ## check if the stacks is empty
    def isEmpty(self):
        return self.items == []
    
    ## insert the item passed as an arg at 0 index
    def enqueue(self, item):
        self.items.insert(0, item)
      
    ## remove and returns the item
    def dequeue(self):
        return self.items.pop()
    
    ## return the length of the stack
    def length(self):
        return len(self.items)
    
    ## displays the items in queue
    def display(self):
        print(self.items)
    
    
## Testing 

## Creating stack object 
queue = Queue()

## Checking if its empty
queue.isEmpty()

## Adding items
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

## Check the length of the stack
queue.length()

## Removing the item
queue.dequeue()

## Check the length of the stack
queue.length()
