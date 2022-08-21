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
     
from doubly_linked_list_class import DoublyLinkedList

## Creating linked-list object          
dll = DoublyLinkedList()

## Adding Node to head
dll.addNodeHead(4)
dll.addNodeHead(3)
dll.addNodeHead(2)
dll.addNodeHead(1)

## Display
dll.display()

## Adding Node to tail
dll.addNodeTail(5)
dll.addNodeTail(6)
dll.addNodeTail(7)
dll.addNodeTail(8)

## Display
dll.display()

## Deleting Node from head
dll.removeNodeHead()
dll.removeNodeHead()

## Display
dll.display()

## Deleting Node from tail
dll.removeNodeTail()
dll.removeNodeTail()

## Display
dll.display()

## Deleting Node from head
dll.removeNodeHead()
dll.removeNodeHead()
dll.removeNodeHead()

## Display
dll.display()

dll.removeNodeHead()

## Display
dll.display()