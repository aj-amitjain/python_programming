#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 17:55:49 2022

@author: Amit Anchalia
"""

'''
Question:
Given a string of words, reverse all the words. 

For example:

Input:

    'This is the best'
    
Output:

    'best the is This'
 
'''

## Method 1
def word_reversal_m1(sent):
    
    sent_token = sent.split()
    
    reverse_sent = ''
    for item in sent_token:
        reverse_sent = ' ' + item + reverse_sent   

    reverse_sent = reverse_sent.lstrip()
    return reverse_sent

## Method 2
def word_reversal_m2(sent):
    
    sent_token = sent.split()
    sent_token = sent_token[::-1]
    
    reverse_sent = ' '.join(sent_token)
    
    return reverse_sent

## Method 3
def word_reversal_m3(sent):
    
    sent_token = sent.split()
    sent_token = reversed(sent_token)
    
    reverse_sent = ' '.join(sent_token)
    
    return reverse_sent    

## Testing
from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        try:
            assert_equal(sol('This is the best'),'best the is This')
            assert_equal(sol(' This is  the best '),'best the is This')
            assert_equal(sol('   Hello World,  how are you   '),'you are how World, Hello')
            assert_equal(sol('1'),'1')
            print("ALL TEST CASES PASSED")
        except:
            raise('ERROR : TEST FAILED')
        
# Run and test
t = ReversalTest()
t.test(word_reversal_m1)
t.test(word_reversal_m2)
t.test(word_reversal_m3)




