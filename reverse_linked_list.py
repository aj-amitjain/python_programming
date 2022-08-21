#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:47:06 2022

@author: Amit Anchalia
"""

'''

Question:
    Write a function to reverse a Linked List in place.
    The function will take in the head of the list as input and return the new head of the list.

'''

from linked_list_class import LinkedList

## Creating another non-circular linked-list 
ll = LinkedList()

ll.addNodeHead(4)
ll.addNodeHead(3)
ll.addNodeHead(2)
ll.addNodeHead(1)

## Displaying the linked-list
ll.display()


def reverse_linked_list(ll):
    
    if ((ll.head == None) or (ll.tail == None)):
        return ll
    
    reversed_ll = LinkedList()
    
    while ll.head != None:
        # reversed_ll.addNodeTail(ll.removeNodeTail()) ## or 
        reversed_ll.addNodeHead(ll.removeNodeHead())

    return reversed_ll



reversed_ll = reverse_linked_list(ll)
reversed_ll.display()
