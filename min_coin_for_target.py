#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:01:43 2022

@author: Amit Anchalia
"""

'''

Question:
    Given a target amount n and a list of distinct coin values, what's the fewest coins needed to make the change amount.

For example:
    If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:
        1. 1+1+1+1+1+1+1+1+1+1
        2. 5+1+1+1+1+1
        3. 5+5
        4. 10

With 1 coin being the minimum amount.

'''
import math
    
def recur_min_coins(target, coin_list):
    
    min_coins = math.inf
    if target in coin_list:
        return 1
    
    else:
        for c in [coin for coin in coin_list if coin < target]:
            
            num_count = 1 + recur_min_coins(target-c, coin_list)
            
            if num_count < min_coins:
                min_coins = num_count
    
    return min_coins

print(recur_min_coins(15, [1, 5, 10]))