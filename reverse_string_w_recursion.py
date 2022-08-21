#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 13:00:29 2022

@author: Amit Anchalia
"""

'''
Question:
    Reverse a string using recursion.

'''

def reverse_string(string):
    
    if len(string) == 1:
        return string
    
    return reverse_string(string[1:]) + string[0] 

## Testing
from nose.tools import assert_equal

class TestReverseString(object):
    
    def test_rev_str(self,solution):
        try:
            assert_equal(solution('hello'),'olleh')
            assert_equal(solution('hello world'),'dlrow olleh')
            assert_equal(solution('123456789'),'987654321')
            print('All test passed!')
        except:
            raise('Error: Test failed')
        
        
# Run Tests
t = TestReverseString()
t.test_rev_str(reverse_string)