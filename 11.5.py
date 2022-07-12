# -*- coding: utf-8 -*-
"""
Created on Sat May 28 12:32:50 2022

@author: 44780
"""

#Two words are “rotate pairs” if you can rotate one of them and get the other (see
#rotate_word in Exercise 8.5).
#Write a program that reads a wordlist and finds all the rotate pairs. Solution: http: //
#thinkpython2. com/ code/ rotate_ pairs. py .
 
fin=open('C:/Users/44780/Desktop/git Think-Py-Solutions/words.txt','r')       

word_dict=dict()
for line in fin:
    word_dict[line.strip().lower()]=0
    
###This is 8.5
import string

alphabet=list(string.ascii_lowercase)
upper_alphabet=list(string.ascii_uppercase)

lowercase_dict={}
uppercase_dict={}

for letter in alphabet:
    lowercase_dict[ord(letter)%97]= letter
    
for letter in upper_alphabet:
    uppercase_dict[ord(letter)%65]= letter

def rotate_letter(letter,num):
    if letter.islower()==True:
        letter_encoded=ord(letter)%97
        return lowercase_dict[(letter_encoded+num)%26]
    else:
        letter_encoded=ord(letter)%65
        return uppercase_dict[(letter_encoded+num)%26]
        

def rotate_word(word, num):
    rotated_word=''
    for letter in word:
        if letter == ' ':
            rotated_word+= ' '
        else:
            rotated_word += rotate_letter(letter, num)
    return rotated_word      

def rotate_pairs(word,word_dict):
    #prints the pairs of words whoch are rotate pairs and how many rotations it takes, word must be in word_dict
    for i in range(14):
        rotated = rotate_word(word, i+1)
        if rotated in word_dict:
            print(word, i, rotated)
            
for word in word_dict:
    rotate_pairs(word, word_dict)

    
    




