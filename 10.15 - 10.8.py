# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:17:37 2021

@author: chapperz
"""

'''This exercise pertains to the so-called Birthday Paradox, which you can read about
at http: // en. wikipedia. org/ wiki/ Birthday_ paradox .
If there are 23 students in your class, what are the chances that two of you have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for
matches. Hint: you can generate random birthdays with the randint function in the random
module.'''

import random

def Has_duplicates(L):
    #L is a list
    check=[]
    output=False
    for char in L:
        if char in check:
            output=True
        check.append(char)
    return output

def Case():
    l=[]
    for i in range(23):
        l.append(random.randint(0,365))
    if Has_duplicates(l)==True:
        return True
    else:
        return False

true_ans=0    
for i in range(1000):
    if Case()==True:
        true_ans=true_ans+1
        
print('The % probibility of at least one shared birthday in a class of 23 people is', 100*true_ans/1000)
    
