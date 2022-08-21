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

class LinkedList(object):
    
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
            self.head = node

    def addNodeTail(self, value):
        
        node = Node(value)
        
        if ((self.head == None) and (self.tail == None)):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node  

    def removeNodeHead(self):
        
        if (self.head == self.tail):
            removed_value = self.head.value
            self.head = None
            self.tail = None
        
        if (self.head != None):
            removed_value = self.head.value
            self.head = self.head.next
        
            return removed_value
            

    def removeNodeTail(self):
        
        if (self.head == self.tail):
            removed_value = self.head.value
            self.head = None
            self.tail = None
            
            return removed_value
        
        if (self.tail != None):
            
            temp = self.head
            # prev = temp
            while(temp.next != None):
                prev = temp
                temp = temp.next
                
            prev.next = None 
            self.tail = prev 
            
            return temp.value

    def make_circular(self):
        self.tail.next = self.head 

    def make_non_circular(self):
        self.tail.next = None   
        
    def length(self):
        
        len_ = 0
        if self.head == None:
            return len_ 
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
                len_ += 1
            
            return len_
            
                
    def display(self):
        
        print("****************")
        temp = self.head
        while(temp != None):
            print("Node: ", temp.value)
            temp = temp.next
            
            if (temp == self.head):
                break
        print("****************")    