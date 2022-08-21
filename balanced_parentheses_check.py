#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 12:22:16 2022

@author: Amit Anchalia
"""

'''
Question:
    Given a string of opening and closing parentheses, check whether it’s balanced. 
    We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.
    Assume that the string doesn’t contain any other character than these, no spaces words or numbers.
    As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. 
    
Example:
    ‘([])’ is balanced but ‘([)]’ is not.

Note:
    You can assume the input string has no spaces.

'''

class Stack(object):
    
    ## initialise the stack
    def __init__(self):
        self.items = []
     
    ## check if the stacks is empty
    def isEmpty(self):
        return self.items == []
    
    ## return top item in the stack
    def peek(self):
        return self.items[len(self.items)-1]
    
    ## insert the item passed as an arg
    def insert(self, item):
        self.items.append(item)
      
    ## remove and returns the item
    def pop(self):
        return self.items.pop()
    
    ## return the length of the stack
    def length(self):
        return len(self.items)
    
    ## displays the items in stack
    def display(self):
        print(self.items)


## Method 1: Using for loop, O(n)
def is_balanced_parentheses_m1(string):
    
    ## Check if the length is odd, definitely there is extra parentheses
    if len(string)%2 != 0:
        return False
    
    stack = Stack()
    
    for p in string:
        if p in '({[':
            stack.insert(p)

        elif p in ')}]':
            ## Check for length before popping
            if stack.length() != 0:
                return False
            
            pop_item = stack.pop()
            
            if ((not ((pop_item == '(') and (p == ')'))) and
                (not ((pop_item == '{') and (p == '}'))) and
                (not ((pop_item == '[') and (p == ']')))):
                    return False
        else:
            return False
    
    if stack.length() != 0:
        return False
    
    return True

## Testing
from nose.tools import assert_equal

class TestBalanceParenthese(object):
    
    def test(self,sol):
        try:
            assert_equal(sol('[](){([[[]]])}('),False)
            assert_equal(sol('[{{{(())}}}]((()))'),True)
            assert_equal(sol('[[[]])]'),False)
            assert_equal(sol('[[[{]])]'),False)
            assert_equal(sol('[([[]])]'),True)
            print('ALL TEST CASES PASSED')
        except:
            raise("ERROR : TEST FAILED")
        
# Run Tests
t = TestBalanceParenthese()
t.test(is_balanced_parentheses_m1)