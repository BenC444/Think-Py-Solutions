# -*- coding: utf-8 -*-
"""
Created on Sat May 28 12:32:50 2022

@author: 44780
"""

# Exercise 11.4. If you did Exercise 10.7, you already have a function named has_duplicates that
# takes a list as a parameter and returns True if there is any object that appears more than once in the
# list.
# Use a dictionary to write a faster, simpler version of has_duplicates.

def Has_duplicates(L):
    #L is a list
    check=[]
    output=False
    
    for char in L:
        
        if char in check:
            output=True
        
        check.append(char)
    return output

def Has_duplicates2(L):
    #L is a list
    d=dict()
    for i in L:
        d[i]=0
    if len(d)==len(L):
        return False
    else:
        return True
        
