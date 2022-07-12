# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:52:27 2022

@author: 44780
"""

'''Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict'''

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def invert_dict2(d):
    '''this also inverts a dictionary'''
    d2={}
    for key in d:
        value=d[key]
        d2[d.setdefault(key,value)]=key
    return d2

d3={}

for i in range(5):
    d3[i]=i+1

print(invert_dict2(d3),d3)
    