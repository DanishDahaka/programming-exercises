#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import islice

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def save_The_Prisoner(n, m, s):
    # Write your code here
    
    # n==5, m==2, s==1 -> 2 2%5 == 2 (2+0)
    
    #5 2 2 -> 3.    2%5 == 2 +2 -1
    
    # n==7, m==19, s==2 -> 6 19%7 == 5 (5+1)
    
    # n== 3, m== 7, s==3 -> 3 | 7%3 == 1 + 3 - 1 == 3
    
    # create seats
    seats = (i+1 for i in range(n))
    
    # 5 278162896 2 -> 2 
    if m%n == 0:
        return n
    else:
        
        #print(list(seats))
        amount_movement = m%n
        print(f'this is movement {amount_movement}')
        print(f'this is s: {s}')
        print(f'this is s+amount_movement: {s+amount_movement}')


        #print(f'here comes islice: {list(islice(seats, s+amount_movement))}')
        
        return next(islice(seats, s+amount_movement-2, None))
         
    
    
    

if __name__ == '__main__':
    print(save_The_Prisoner(5,2,1))
    print(save_The_Prisoner(5,2,2))
    print(save_The_Prisoner(352926151, 380324688, 94730870))

    #352926151 380324688 94730870 -> 122129406
