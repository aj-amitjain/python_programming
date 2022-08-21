#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 17:30:14 2022

@author: Amit Anchalia
"""

'''
Question:
    Create a fibonacci series : 0,1,1,2,3,5,8,13,21

'''

## Method 1:  Using loop, O(n)
def fibonacci_m1(n):
    

    fibonacci_series = [0, 1]
    
    if (n == 0) or (n == 1):
        return fibonacci_series[:n-1]
    
    else:
        f1 = fibonacci_series[0]
        f2 = fibonacci_series[1]
        while n > 2:
           temp =  f1+f2
           f1 = f2 
           f2 = temp
           fibonacci_series.append(temp)
           n -= 1
    
    return fibonacci_series

## Method 2:  Using recursion, O(2^n)
def fibonacci_m2(n):
    
    def rev_fibonacci(n):
        if (n == 0) or (n == 1):
            return n    
        else:
            f = rev_fibonacci(n-1) + rev_fibonacci(n-2)
            return f
    
    fibonacci_series = []
    
    for i in range(n):
        fibonacci_series.append(rev_fibonacci(i))

    return fibonacci_series


## Testing 
from nose.tools import assert_equal

class TestFibonacciSeries(object):
    
    def Test_fibonacci_series(self,sol):
        
        try:
            assert_equal(sol(7),[0, 1, 1, 2, 3, 5, 8])
            assert_equal(sol(8),[0, 1, 1, 2, 3, 5, 8, 13])
        
            print('All test passed.')
        except:
            raise("Error: test failed")


# Run Tests
t = TestFibonacciSeries()
t.Test_fibonacci_series(fibonacci_m1)
t.Test_fibonacci_series(fibonacci_m2)