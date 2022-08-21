#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:14:56 2022

@author: Amit Anchalia
"""


'''

Question:
    Implement linked-list 

'''
     
from linked_list_class import LinkedList

## Creating linked-list object          
ll = LinkedList()

## Adding Node to head
ll.addNodeHead(4)
ll.addNodeHead(3)
ll.addNodeHead(2)
ll.addNodeHead(1)

## Display
ll.display()

## Adding Node to tail
ll.addNodeTail(5)
ll.addNodeTail(6)
ll.addNodeTail(7)
ll.addNodeTail(8)

## Display
ll.display()

## Deleting Node from head
ll.removeNodeHead()
ll.removeNodeHead()

## Display
ll.display()

## Deleting Node from tail
ll.removeNodeTail()
ll.removeNodeTail()

## Display
ll.display()

## Deleting Node from head
ll.removeNodeHead()
ll.removeNodeHead()
ll.removeNodeHead()

## Display
ll.display()

ll.removeNodeHead()

## Display
ll.display()
