# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:35:03 2022

@author: 44780
"""
'''Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary'''

fin=open('/Users/44780/Desktop/git Think-Py-Solutions/words.txt')

ans={}
def keywords():
    '''this reads words in as keys in the dictionary ans'''
    for word in fin:
        ans[word]='a'
        
keywords()
