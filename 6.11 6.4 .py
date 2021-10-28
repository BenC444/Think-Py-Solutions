# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:24:25 2021

@author: Ben Chapman
"""
"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case"""



def Is_power(a,b):
    '''a and b should be non zero positive integers. I return True for all a=1 as any number to the power of 0 is 1'''
    if a//b == 1 or a==1:
        return True
    elif a%b ==0:    
      print('calls is_power for ', (int(a/b),b))
      return Is_power(int(a/b),b)
    else:
        return False

