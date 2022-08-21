#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 10:50:19 2022

@author: Amit Anchalia
"""

'''
Question:
Given an integer array, output count of all the unique pairs that sum up to a value k.

Input:
    arr: [1,3,2,2]
    k: 4

Output:
    2 

Explanation:
    (1,3) == 4 
    (2,2) == 4 
so, two pairs
 
'''
## Method 1
def get_pair_sum_m1(arr, k):
    
    pair_lists = [(min(i, j), max(i, j)) for index, i in enumerate(arr) for j in arr[index+1:] if (i+j == k)]
    return pair_lists 


# print(get_pair_sum_m1([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10))

def get_pair_count_m1(arr, k):
    
    if len(arr) <= 1:
        return None 
    
    list_ = get_pair_sum_m1(arr, k)
    return len(list_)


## Method 2
def get_pair_count_m2(arr, k):
    
    if len(arr) <= 1:
        return None
    
    seen = set()
    pairs = set()

    for num in arr:
        
        target = k - num
        
        if target not in seen:
            seen.add(num)
            
        else:
           pairs.add((min(num, target), max(num, target)))
    
    # print(pairs)
    return len(pairs) 

# print(get_pair_count_m2([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10))

## Testing
from nose.tools import assert_equal

class TestPairSum(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t = TestPairSum()
t.test(get_pair_count_m1)
t.test(get_pair_count_m2)


