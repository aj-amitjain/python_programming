#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 14:30:33 2022

@author: Amit Anchalia
"""

'''

Question :  

Given an array of integers (positive and/or negative) find the largest continuous sum.

'''

## Method 1: O(n^2)
def get_largest_cont_sum_m1(list_):
    
    import math
    l_c_sum = - math.inf
    
    temp_sum = 0
    for index, item_1 in enumerate(list_):
        for item_2 in list_[index:]:
            temp_sum += item_2
            l_c_sum = max(temp_sum, l_c_sum)
            
        temp_sum = 0 
        
    return l_c_sum


## Method 2: O(n)
def get_largest_cont_sum_m2(list_):
    
    import math
    l_c_sum = -math.inf
    len_n = len(list_)
    
    temp_sum = 0
    for index in range(int(len_n/2)+1):
        sum_1 = sum(list_[index:])
        sum_2 = sum(list_[:(len_n-index-1)])
        sum_3 = sum(list_[index:(len_n-index-1)])

        l_c_sum = max(sum_1, sum_2, sum_3, l_c_sum)

    return l_c_sum




from nose.tools import assert_equal

class TestLargestContSum(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print('ALL TEST CASES PASSED')
        
#Run Test
t = TestLargestContSum()
t.test(get_largest_cont_sum_m1)
t.test(get_largest_cont_sum_m2)


sum([1,2,-1,3,4,-1])
