# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:40:45 2021

@author: chapperz
"""
'''
What is the output of the following program? Draw a stack diagram that shows the
state of the program when it prints the result.
def recurse(n, s):
if n == 0:
print(s)
else:
recurse(n-1, n+s)
recurse(3, 0)
1. What would happen if you called this function like this: recurse(-1, 0)?

A= runtime error/ max recursion depth becasue the base case is never satisfied

2. Write a docstring that explains everything someone would need to know in order to use this
function (and nothing else).
'''



#this function sums integers up to the value n
def Recurse(n, s):
    """input n as a positive integer"""
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
        
