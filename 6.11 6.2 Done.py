# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:11:41 2021

@author: Ben Chapman
"""


'''
Exercise 6.2. The Ackermann function, A(m, n)
n + 1 if m = 0
A(m − 1, 1) if m > 0 and n = 0
A(m − 1, A(m, n − 1)) if m > 0 and n > 0.


See http: // en. wikipedia. org/ wiki/ Ackermann_ function . Write a function named ack
that evaluates the Ackermann function. Use your function to evaluate ack(3, 4), which should be
125. What happens for larger values of m and n? - for larger values of M and N it reaches max recursion depth,
 I think this is because it has two recursions in the final elif and that goes to deep, 
 (I can't think of a get aroud for that problem?)'''


def Ack(m,n):
    '''m and n are non-negitive integers'''
    if m==0:
        return n+1
    elif m>0 and n==0:
        return Ack(m-1,1)
    elif m>0 and n>0:
        return Ack(m-1,Ack(m,n-1))
    
print(Ack(1,2))
    
    