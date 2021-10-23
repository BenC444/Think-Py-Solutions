# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 02:33:21 2021

@author: Ben Chapman
'"""
'''
Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt that
takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of
a.
To test it, write a function named test_square_root that prints a table like this:
a mysqrt(a) math.sqrt(a) diff
- --------- ------------ ----
1.0 1.0 1.0 0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0.0
4.0 2.0 2.0 0.0
5.0 2.2360679775 2.2360679775 0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0 3.0 0.0
The first column is a number, a; the second column is the square root of a computed with mysqrt;
the third column is the square root computed by math.sqrt; the fourth column is the absolute value
of the difference between the two estimates.
'''
import math 

def mysqrt(a):
    '''outputs a float input should be a positive integer'''
    x=a/2
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        if x==0:
            break
        x = y
    return x



def test_square_root():
    print('a mysqrt(a)            math.sqrt(a)      diff \n- ---------            ------------      ----')
    for i in range(9):
        print(i+1,str(mysqrt(i+1)).ljust(20),
              str(math.sqrt(i+1)).ljust(18), 
              abs(mysqrt(i+1))-math.sqrt(i+1))


test_square_root()
