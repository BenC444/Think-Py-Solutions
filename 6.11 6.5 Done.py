# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 21:33:16 2021

@author: chapperz
"""

'''
The greatest common divisor (GCD) of a and b is the largest number that divides
both of them with no remainder.

One way to find the GCD of two numbers is based on the observation that if r is the remainder when
a is divided by b, then gcd(a, b) = gcd(b,r). As a base case, we can use gcd(a, 0) = a.
Write a function called gcd that takes parameters a and b and returns their greatest common divisor.

Credit: This exercise is based on an example from Abelson and Sussman’s Structure and Interpretation of Computer Programs.
'''


def GCD(a,b):
    'a and b are positive integers'
    if b==0:
        return a
    else:    
        remainder=a%b
        print('remainder is: ',remainder)
        return GCD(b,remainder)
    

    
    
    