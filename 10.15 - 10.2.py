# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:12:41 2021

@author: chapperz
"""

'''Write a function called cumsum that takes a list of numbers and returns the cumulative sum; that is,
 a new list where the ith element is the sum of the first i + 1 elements from the
original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]'''


def Cumsum(L):
    #L should be a list
    output=[]
    cumilative=0
    for element in L:
        cumilative+=element
        output.append(cumilative)
    return output
        
t=[1,2,3,69]
print(Cumsum(t))