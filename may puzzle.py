# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:42:18 2021

@author: 44780
"""

import numpy as np

fin = open('words.txt')

#homemade functions to help

def unique_char(word):
    #this returns the unique charagcters of word
    word=word.replace(" ","")
    return ''.join(set(word.strip()))


def is_in(letter,string):
    counter=0
    output=True
    for char in string:
        if letter==char:
            counter+=1
    if counter==0:
        output=False
    return output
        
#this returns true if the letter is in the string

def uses_only(word,letters):
    #returns true if word only contains letters in 'letters'
    unique_letters = unique_char(letters)
    y=0
    for char in word:
        #print(char)
        if is_in(char,unique_letters) == False:
            return False
    return True


#setup for the problem


solution_dict = {12:"a",7:"t"}

letters_string="acdehinoprst"

grid=np.array([[12,11,12,1,7],[9,False,5,False,10],[7,2,3,8,6],
               [4,False,10,False,9],[5,12,9,6,11]])

#print(grid[0][0]) will return the 1st element of 1st row


def word(legnth):
    ###will create a list of words of a specified legnth
    LW=[]
    for word in fin:
        if len(word) == legnth+1:
            LW.append(word)
    return LW

lw5 = word(5)

#my goal is to generate a new grid from a dictionary - I will do a smaller version first lulw
poss_words=[]
for word in lw5:
    if uses_only(word,letters_string)==True:
        poss_words.append(word)
        
        
        
        
        
        
        
        
        
        
        