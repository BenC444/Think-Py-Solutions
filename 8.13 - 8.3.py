# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:45:56 2021

@author: chapperz
"""

'''A string slice can take a third index that specifies the “step size”; that is, the number
of spaces between successive characters. A step size of 2 means every other character; 3 means every
third, etc.
80 Chapter 8. Strings
>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
Use this idiom to write a one-line version of is_palindrome from Exercise 6.3'''

def is_palindrome2(word):
    
    if word[::-1]==word:
        return True
    else:
        return 'that is sooo... not a palindrome'

print(is_palindrome2('lovel'))    

