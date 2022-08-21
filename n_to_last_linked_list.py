#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 12:37:08 2022

@author: Amit Anchalia
"""

'''
Question:
    Write a function that takes an integer value n and then returns the nth to last node in the linked list.

'''

from linked_list_class import LinkedList

## Creating linked-list object          
ll = LinkedList()

## Adding Node to head
ll.addNodeHead(6)
ll.addNodeHead(5)
ll.addNodeHead(4)
ll.addNodeHead(3)
ll.addNodeHead(2)
ll.addNodeHead(1)

## Display
ll.display()


def get_n_to_last_ll(ll, n):
    
    
    if n > ll.length():
        return None
    
    if n == 0:
        return ll
    
    current_pos = 0 
    temp = ll.head
    
    ll_red = LinkedList()
    while current_pos != n:
        temp = temp.next
        current_pos += 1
     
    while temp != None:
        
        ll_red.addNodeTail(temp.value)
        temp = temp.next
    
    return ll_red


## Testing with n = 0
ll_red_0 = get_n_to_last_ll(ll, 0)
ll_red_0.display()

## Testing with n = 3
ll_red_3 = get_n_to_last_ll(ll, 3)
ll_red_3.display()