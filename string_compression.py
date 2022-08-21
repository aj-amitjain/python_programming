#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 18:29:53 2022

@author: Amit Anchalia
"""

'''
Question:
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
 
The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

'''

# Method 1
def compress_str(str_):
    
    if ((str_ == '') or (str_ == ' ')):
        return ''
    
    from collections import Counter
    
    compressed_str = ''
    counter = Counter(list(str_))
    
    for item in counter:
        compressed_str += item + str(counter[item])
    
    return compressed_str



## Testing
from nose.tools import assert_equal

class TestCompressStr(object):

    def test(self, sol):
        try:
            assert_equal(sol(''), '')
            assert_equal(sol(' '), '')
            assert_equal(sol('AABBCC'), 'A2B2C2')
            assert_equal(sol('AAAaaa'), 'A3a3')
            assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
            print('ALL TEST CASES PASSED')
        except :
            raise('ERROR : TEST FAILED')
        

# Run Tests
t = TestCompressStr()
t.test(compress_str)