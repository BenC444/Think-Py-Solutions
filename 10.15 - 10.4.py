# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:26:18 2021

@author: chapperz
"""

'''
Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None. For example:
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
'''
def Chop(L):
    #L is a list
    L.pop()
    L.pop(0)
    
t=[1,2,4,5]
Chop(t)
print(t)