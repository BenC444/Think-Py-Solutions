# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 08:37:31 2021

@author: chapperz
"""

'''
Write a function called estimate_pi that uses this formula to compute and return an estimate of
π. It should use a while loop to compute terms of the summation until the last term is smaller than
1e-15 (which is Python notation for 10**−15). You can check the result by comparing it to math.pi
'''
import math

def fact(n):
    if n==0:
        return 1
    else:
        recurse=fact(n-1)
        result = n* recurse
        return result    
    
def estimate_pi():
    k=0
    factor=2*math.sqrt(2)/9801
    total=0
    while True:
        num=(fact(4*k))*(1103+26390*k)
        denom=((fact(k))**4 )*(396**(4*k))
        sum_term=factor*num/denom
        print('k=',k, 'term=',sum_term)
        total+=sum_term
        k=k+1
        if abs(sum_term)<1e-15:
            print('pi has been approximated at:', total**(-1), 'pi is actually:', math.pi)
            break


#print(fact(6))
      
estimate_pi()



    