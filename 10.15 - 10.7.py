# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:13:13 2021

@author: chapperz
"""

'''Write a function called has_duplicates that takes a list and returns True if there
is any element that appears more than once. It should not modify the original list.'''

def Has_duplicates(L):
    #L is a list
    check=[]
    output=False
    
    for char in L:
        
        if char in check:
            output=True
        
        check.append(char)
    return output

t=[1,2,3,4,1]
k=[4,6,3,2,1,]

print(Has_duplicates(t))