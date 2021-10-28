# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:37:01 2021

@author: chapperz
"""

'''Exercise 5.3. If you are given three sticks, you may or may not be able to arrange them in a triangle.
For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not
be able to get the short sticks to meet in the middle. For any three lengths, there is a simple test to
see if it is possible to form a triangle:
If any of the three lengths is greater than the sum of the other two, then you cannot
form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
form what is called a “degenerate” triangle.)
1. Write a function named is_triangle that takes three integers as arguments, and that prints
either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks
with the given lengths.
2. Write a function that prompts the user to input three stick lengths, converts them to integers,
and uses is_triangle to check whether sticks with the given lengths can form a triangle.
'''

def Is_triangle(a,b,c):
    '''abc are not in order, they are integers'''
    sides=[a,b,c]
    
    if a>b and a>c:
        hypotenuse=a
        sides.remove(a)
    
    elif b>a and b>c:
        hypotenuse=b
        sides.remove(b)
    
    else:
        hypotenuse=c
        sides.remove(c)
        
    if hypotenuse**2 == int(sides[1])**2 + int(sides[0])**2:
        print('yes')
    else:
        print('no')
    

def Input_is_triangle():
    '''a,b,c should be integers'''
    a=int(input('legnth a:'))
    b=int(input('legnth b:'))
    c=int(input('legnth c:'))
    Is_triangle(a,b,c)
    
Input_is_triangle()
    
