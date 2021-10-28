# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:52:57 2021

@author: chapperz
"""

'''The following functions are all intended to check whether a string contains any
lowercase letters, but at least some of them are wrong. For each function, describe what the function
actually does (assuming that the parameter is a string).
'''

def any_lowercase1(s):
    #this function checks if the first character in a string is lowercase, but not the subsequent ones 
    for c in s:
        if c.islower():
            return True
        else:
            return False 
        
def any_lowercase2(s):
    #this function checks if the character 'c' is lowercase as many times as there are letters in s,
    #it doesn't return a boolean
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def bool_output_check(f,x):
    if f(x)==True or f(x)==False:
        print("it's a boolean'")
    else:
        print('faker boolean detected!')

def any_lowercase3(s):
    #this funtion only checks if the first character is lower and returns true or false appropriately
    for c in s:
        flag = c.islower()
        return flag
    
def any_lowercase4(s):
    #I have now learned that False or True and true or false returns True, so the first line in the for loop would
    #update the flag to true if a single letter in s is lower, However as it returns flag inside the loop it will 
    #only check the first letter.
    flag = False
    for c in s:
        flag = flag or c.islower()
        return flag

def any_lowercase5(s):
    #for the first character in s the function will return False if it's upper and true if it's lower.
    #calling return too early pulls the function ont of the loop so it never checks subseuent letters
    for c in s:
        if not c.islower():
            return False
        return True