# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:47:21 2021

@author: chapperz
"""
'''
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.'''


def Is_anagram(word_1,word_2):
    word1_list=list(word_1)    
    word2_list=list(word_2)
    word1_list.sort()
    word2_list.sort()
    if word2_list==word1_list:
        return True
    
print(Is_anagram('balls','lbasl'))

