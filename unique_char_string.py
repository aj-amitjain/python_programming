#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:44:49 2022

@author: Amit Anchalia
"""

'''
Question:
Given a string,determine if it is compreised of all unique characters.

For example: 
    The string 'abcde' has all unique characters and should return True.
    The string 'aabcde' contains duplicate characters and should return false.

'''

## Method 1: Using Counter, O(n)
def is_unique_char_str_m1(string):
    
    if ((string == '') or (string == ' ')):
        return True
    
    if (string == None):
        return False
        
    from collections import Counter
    
    counter = Counter(string)
    
    items = counter.values()
    duplicate = not any([item > 1 for item in items])

    return duplicate


## Method 2: Using for loop, O(n) 
def is_unique_char_str_m2(string):
    
    if ((string == '') or (string == ' ')):
        return True
    
    if (string == None):
        return False
        
    set_ = []
    
    for item in list(string):
        if item in set_:
            return False
        else:
            set_.append(item)

    return True


## Method 3:  Using sort, O(nlogn) 
def is_unique_char_str_m3(string):
    
    if ((string == '') or (string == ' ')):
        return True
    
    if (string == None):
        return False
        
    list_ = list(string)
    set_ = list(set(list_))

    print(list_, set_)
    return (list_.sort() == set_.sort())


## Testing
from nose.tools import assert_equal

class TestUniqueChar(object):
    
    def testString(self, sol):
        try:
            assert_equal(sol(''), True)
            assert_equal(sol('good'), False)
            assert_equal(sol('abcdefg'), True)
            print('ALL TEST CASES PASSED')
        except:
            raise('ERROR : TEST FAILED')

        
## Run Tests
t = TestUniqueChar()
t.testString(is_unique_char_str_m1)
t.testString(is_unique_char_str_m2)
t.testString(is_unique_char_str_m3)
