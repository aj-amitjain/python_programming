#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 13:09:49 2022

@author: Amit Anchalia
"""

'''

Question :  

Consider an array of non-negative integers. 
A second array is formed by shuffling the elements of the first array and deleting a random element.
Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

    array_1: [1,2,3,4,5,6,7]
    array_2: [3,7,2,1,4,6]
    
Output: 
    5 is the missing number
    
'''

## Method 1: O(n^2)
def get_missing_element_m1(list_1, list_2):
    
    for item in list_2:
        list_1.remove(item)
        
    return list_1[0]


## Method 2: O(nlogn)
def get_missing_element_m2(list_1, list_2):
    
    list_1.sort()  ## O(nlogn)
    list_2.sort()  ## O(nlogn)
    
    ## O(n)
    for i, j in zip(list_1, list_2):
        if i!=j:
            return i
        
    return None

## Method 3: O(nlogn)
def get_missing_element_m3(list_1, list_2):
    
    from collections import Counter
    
    list_2_counter = Counter(list_2)

    for i in list_1:
        if list_2_counter[i] == 0:
            return i
        
        list_2_counter[i] -= 1
        
    return None

## Method 4: O(n)
def get_missing_element_m4(list_1, list_2):
    
    res = 0 
    for item in list_1 + list_2:
        res ^= item
    
    return res


## Testing
from nose.tools import assert_equal

class TestMissingElement(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

# Run test
t = TestMissingElement()
t.test(get_missing_element_m1)
t.test(get_missing_element_m2)
t.test(get_missing_element_m3)
t.test(get_missing_element_m4)
