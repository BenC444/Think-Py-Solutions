# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:09:18 2021

@author: chapperz
"""

'''. Write a function called nested_sum that takes a list of lists of integers and adds up
the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21'''

def Nested_sum(nested_list):
    #nested_list should be a list 
    output=0
    for i in nested_list:
        for a in i:
            output+=a
    return(output)
    
t =[[1,2,9],[3],[4,5,6]]


print(Nested_sum(t))
            