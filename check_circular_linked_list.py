#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:22:08 2022

@author: Amit Anchalia
"""

'''

Question:

    Given a singly linked list, write a function which takes in the first node in a singly linked list 
    and returns a boolean indicating if the linked list contains a "cycle".

    A cycle is when a node's next point actually points back to a previous node in the list.
    This is also sometimes known as a circularly linked list.


'''
    

from linked_list_class import LinkedList

def check_circular_linked_list(ll):
    
    return ll.tail.next == ll.head


## Creating a circular linked-list 
a = LinkedList()

## Adding Node to head
a.addNodeHead(4)
a.addNodeHead(3)
a.addNodeHead(2)
a.addNodeHead(1)

## Making it circular
a.make_circular()

## Displaying the linked-list
a.display()


## Creating another non-circular linked-list 
b = LinkedList()

b.addNodeHead(4)
b.addNodeHead(3)
b.addNodeHead(2)
b.addNodeHead(1)

## Displaying the linked-list
b.display()


## Testing 
from nose.tools import assert_equal

class TestCircularLinkedList():
    
    def test_circular_linked_list(self, sol):
        try:
            assert_equal(sol(a), True)
            assert_equal(sol(b), False)
            print("All test passed !!")
        except:
            raise("Error, Test Failed")
            
t = TestCircularLinkedList() 
t.test_circular_linked_list(check_circular_linked_list)
      