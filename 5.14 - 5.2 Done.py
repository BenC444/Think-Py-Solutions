# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:26:49 2021

@author: Ben Chapman
"""

'''Exercise 5.2. Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
a^n + b^n = c^n
for any values of n greater than 2.
1. Write a function named check_fermat that takes four parameters—a, b, c and n—and
checks to see if Fermat’s theorem holds. If n is greater than 2 and the theorem holds

the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.”
2. Write a function that prompts the user to input values for a, b, c and n, converts them to
integers, and uses check_fermat to check whether they violate Fermat’s theorem.
'''

def Check_fermat(a,b,c,n):
    '''inputs are integers'''
    L=a**(n) + b**(n)
    R=c**(n)
    if L==R:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn’t work.")
        


def Prompt_fermat():
    '''Takes values, converts into integers and removes invalid entries.'''
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    n=int(input('n='))
    while True:
        if n<2:
            print ('Invalid n')
            return 'Invalid n'
        if a<=0:
            print ('Invalid a')
            return 'Invalid a'
        if b<=0:
            print ('Invalid b')
            return 'Invalid b'
        if c<=0:
            print ('Invalid c')
            return 'Invalid c'
    Check_fermat(a,b,c,n)

    
    
Prompt_fermat()