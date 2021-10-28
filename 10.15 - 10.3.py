# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:19:38 2021

@author: chapperz
"""

'''Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. For example:
>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]'''

def Middle(L):
    #L is a list
    return L[1:len(L)-1]

t=[1,2,3,4,5,6,78,8]
print(Middle(t))