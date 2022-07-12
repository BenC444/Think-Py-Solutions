# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


'''Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?'''


def avoids(word,banned):
    #this returns False is word contains a banned letter, True if it doesn't.
    output=True
    for l in banned:
        if l in word:
            output = False
    return output

print(avoids('Hello','e'))