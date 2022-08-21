#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 12:10:14 2022

@author: Amit Anchalia
"""

'''
Question:
    Implement deque.

Notes:
    1. Enqueue (Insert)
    2. Dequeue (Pop)
    3. isEmpty
    4. Length
    5. Create  

'''


class Deque(object):
    
    ## initialise the stack
    def __init__(self):
        self.items = []
     
    ## check if the stacks is empty
    def isEmpty(self):
        return self.items == []
    
    ## insert the item passed as an arg at 0 index
    def enqueueFront(self, item):
        self.items.insert(0, item)
    
    ## insert the item passed as an arg at n-1 index
    def enqueueRear(self, item):
        self.items.append(item)
        
    ## remove and returns the item at 0 index
    def dequeueFront(self):
        return self.items.pop(0)
    
    ## remove and returns the item at n-1 index
    def dequeueRear(self):
        return self.items.pop()
    
    ## return the length of the stack
    def length(self):
        return len(self.items)
    
    ## displays the items in deque
    def display(self):
        print(self.items)
    
    
## Testing 

## Creating stack object 
deque = Deque()

## Checking if its empty
deque.isEmpty()

## Adding items from front
deque.enqueueFront(1)
deque.enqueueFront(2)
deque.enqueueFront(3)

## Display deque
deque.display()

## Adding items at read
deque.enqueueRear(0)
deque.enqueueRear(-1)
deque.enqueueRear(-2)

## Display deque
deque.display()

## Check the length of the stack
deque.length()

## Removing the item from rear
deque.dequeueRear()

## Removing the item from front
deque.dequeueFront()

## Display deque
deque.display()

## Check the length of the stack
deque.length()
