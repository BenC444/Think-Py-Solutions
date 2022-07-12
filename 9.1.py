# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:00:36 2022

@author: 44780
"""

fin=open('C:/Users/44780/Desktop/git Think-Py-Solutions/words.txt')

for line in fin:
    if len(line)>19:
        print(line)
    else:
        pass
