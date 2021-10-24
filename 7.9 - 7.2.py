# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:51:50 2021

@author: chapperz
"""

'''The built-in function eval takes a string and evaluates it using the Python interpreter. For example:
>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>
Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of the last expression it
evaluated.'''

def Eval_loop():
    while True:    
        text=input('>')
        if text=='done':
            print(l[-1])
            break
        l=[]
        e=eval(text)
        print('text is: ',text)
        print('the evaluated text is: ',e)
        l.append(e)
    
Eval_loop()