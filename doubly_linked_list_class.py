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

class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList(object):
    
    def __init__(self):
        
        self.head = None
        self.tail = None
                
    def addNodeHead(self, value):
        
        node = Node(value)
        
        if ((self.head == None) and (self.tail == None)):
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def addNodeTail(self, value):
        
        node = Node(value)
        
        if ((self.head == None) and (self.tail == None)):
            self.head = node
            self.tail = node
        else:                
            self.tail.next = node
            node.prev = self.tail
            self.tail = node  

    def removeNodeHead(self):
        
        if (self.head == self.tail):
            removed_value = self.head.value
            self.head = None
            self.tail = None
        
        if (self.head != None):
            temp = self.head
            removed_value = temp.value
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        
            return removed_value
            

    def removeNodeTail(self):
        
        
        if (self.head == self.tail):
            removed_value = self.head.value
            self.head = None
            self.tail = None
        
        if (self.tail != None):
            
            removed_value = self.tail.value 
            temp = self.tail.prev
            temp.next = None
            self.tail.prev = None
            self.tail = temp
            
        return removed_value

    def make_circular(self):
        self.tail.next = self.head 

    def make_non_circular(self):
        self.tail.next = None       
                
    def display(self):
        
        print("****************")
        temp = self.head
        while(temp != None):
            print("Node: ", temp.value)
            temp = temp.next
            
            if (temp == self.head):
                break
        print("****************")    