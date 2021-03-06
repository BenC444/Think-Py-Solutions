# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 16:36:50 2021

@author: chapperz
"""
'''
5. A Caesar cypher is a weak form of encryption that involves “rotating” each letter by
a fixed number of places. To rotate a letter means to shift it through the alphabet, wrapping around
to the beginning if necessary, so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.
To rotate a word, rotate each letter by the same amount. For example, “cheer” rotated by 7 is “jolly”
and “melon” rotated by -10 is “cubed”. In the movie 2001: A Space Odyssey, the ship computer
is called HAL, which is IBM rotated by -1.
Write a function called rotate_word that takes a string and an integer as parameters, and returns
a new string that contains the letters from the original string rotated by the given amount.
You might want to use the built-in function ord, which converts a character to a numeric code, and
8.13. Exercises 81
chr, which converts numeric codes to characters. Letters of the alphabet are encoded in alphabetical
order, so for example:
>>> ord('c') - ord('a')
2
Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for upper case
letters are different.
Potentially offensive jokes on the Internet are sometimes encoded in ROT13, which is a Caesar
cypher with rotation 13. If you are not easily offended, find and decode some of them. 
'''
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

print('What did the mother broom say to the baby broom?', rotate_word('Vgf gvzr gb tb gb fjrrc',13))