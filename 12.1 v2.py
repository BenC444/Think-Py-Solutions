# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:57:15 2022

@author: 44780
"""

'''Write a function called most_frequent that takes a string 
and prints the letters in decreasing order of frequency.
'''
def most_frequent(string):
    l=[]
    t=tuple(string)
    for char in t:
        num=t.count(char)
        l.append((num,char))
    l.sort()
    l2=[]
    for ele in reversed(l):
        l2.append(ele[1])
    l2=list(dict.fromkeys(l2))
    return l2

print(most_frequent('elo hell'))