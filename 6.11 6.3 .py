# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:55:13 2021

@author: chapperz
"""

'''A palindrome is a word that is spelled the same backward and forward, like “noon”
and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the
middle is a palindrome.
The following are functions that take a string argument and return the first, last, and middle letters:
def first(word):
return word[0]
def last(word):
return word[-1]
def middle(word):
return word[1:-1]
We’ll see how they work in Chapter 8.
1. Type these functions into a file named palindrome.py and test them out. What happens if
you call middle with a string with two letters? One letter? What about the empty string,
which is written '' and contains no letters?
2. Write a function called is_palindrome that takes a string argument and returns True if it
is a palindrome and False otherwise. Remember that you can use the built-in function len
to check the length of a string'''


'''these all take string inputs'''
def First(word):
    return word[0]

def Last(word):
    return word[-1]

def Middle(word):
    return word[1:-1]



def is_palindrome(word):
    '''word is a string'''
    for i in range (int(len(word)/2)):
        print('    '*i ,'start', word[i])
        print('    '*i ,'end', word[-1-i])
        if word[i]!=word[-1-i]:
            return False
    return True
