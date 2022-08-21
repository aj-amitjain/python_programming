#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 13:12:19 2022

@author: Amit Anchalia
"""

'''
Question:
    Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.

For example:
    For s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

Note: If a character is repeated, treat each occurence as distinct.

'''

def string_premutations(string):
    
    str_list = []
    
    ## Based case - return if it a single digit.
    if len(string) == 1:
        str_list = [string]
        
    else:
        
        ## Taking a letter at a time
        for index, item in enumerate(string):
            ## Creating premutation with remaining letters
            for premutations in string_premutations(string[:index] + string[index+1:]):
                ## Appending the letter and all the permutations created
                str_list += [item + premutations]
    
    return str_list


## Testing 
from nose.tools import assert_equal

class TestStringPermutation(object):
    
    def test_string_permutation(self,solution):
        
        try:
            assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
            assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))
            assert_equal(sorted(solution('abcd')),sorted(['abcd', 'abdc', 'acbd', 'acdb', 'adbc',
                                                          'adcb', 'bacd', 'badc', 'bcad', 'bcda',
                                                          'bdac', 'bdca', 'cabd', 'cadb', 'cbad',
                                                          'cbda', 'cdab', 'cdba', 'dabc', 'dacb',
                                                          'dbac', 'dbca', 'dcab', 'dcba']))
        
            print('All test passed.')
        except:
            raise("Error: test failed")


# Run Tests
t = TestStringPermutation()
t.test_string_permutation(string_premutations)