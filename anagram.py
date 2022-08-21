#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 10:13:59 2022

@author: Amit Anchalia
"""

'''

Question : 
Given two strings, check to see if they are anagrams.
An anagram is when the two strings can be written using the exact same letters 
Note: you can just rearrange the letters to get a different phrase or word

For example:

"God" is an anagram of "dog"
"clint eastwood" is an anagram of "old west action"

'''

## Method 1 : Using list and sort 
def is_anagram_m1(string_1, string_2):
    
    if ((string_1 != None) and (string_2 != None)):
        
        string_1 = string_1.replace(" ", '').lower()
        string_2 = string_2.replace(" ", '').lower()
        
        str_1_list = list(string_1)
        str_2_list = list(string_2)
        if len(str_1_list) ==  len(str_2_list):
            str_1_list.sort()
            str_2_list.sort()
            
            if str_1_list == str_2_list:
                return True
    
    return False


## Method 2 : Using sorted, which directly convert string to list
def is_anagram_m2(string_1, string_2):
    
    if ((string_1 != None) and (string_2 != None)):
        
        string_1 = string_1.replace(" ", '').lower()
        string_2 = string_2.replace(" ", '').lower()
        
        str_1_list = sorted(string_1)
        str_2_list = sorted(string_2)
        if str_1_list == str_2_list:
            return True
    
    return False

## Testing 
from nose.tools import assert_equal
class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('aabbcc','aaccbb'), True)
        assert_equal(sol('aabccc','aaccbb'), False)
        assert_equal(sol('hi world','world hi'), True)
        assert_equal(sol('dog','gods'), False)
        assert_equal(sol('clint eastwood','old west action'), True)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(is_anagram_m1)