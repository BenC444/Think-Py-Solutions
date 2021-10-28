# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:28:56 2021

@author: chapperz
"""

'''Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False'''
def Is_sorted(L):
    #L is a list
    output=True
    for i in range (len(L)):
        if i==len(L)-1:
            return output
        else:
            if L[i]>L[i+1]:
                output=False
    return output
            
t=[1,25,24]
l=['a','b','c']

print(Is_sorted(t))
print(Is_sorted(l))