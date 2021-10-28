# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 12:37:12 2021

@author: chapperz
"""

fin= open('words.txt')

'''Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).'''

for line in fin:
    if len(line.strip())>20:
        print (line)
    
    