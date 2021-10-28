# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:22:05 2021

@author: chapperz
"""
'''
The Koch curve is a fractal that looks something like Figure 5.2. To draw a Koch
curve with length x, all you have to do is
1. Draw a Koch curve with length x/3.
2. Turn left 60 degrees.
3. Draw a Koch curve with length x/3.
4. Turn right 120 degrees.
5. Draw a Koch curve with length x/3.
6. Turn left 60 degrees.
7. Draw a Koch curve with length x/3.
The exception is if x is less than 3: in that case, you can just draw a straight line with length x.
1. Write a function called koch that takes a turtle and a length as parameters, and that uses the
turtle to draw a Koch curve with the given length.
2. Write a function called snowflake that draws three Koch curves to make the outline of a
snowflake
'''

import turtle


bob=turtle.Turtle()

def koch(t,x):
    '''t is a turtle, x is the legnth of the knoch curve'''
    if x<3:
        t.fd(x)
        return
    koch(t,x/3)
    t.lt(60)
    koch(t,x/3)
    t.rt(120)
    koch(t,x/3)
    t.lt(60)
    koch(t,x/3)
    
    
def Snowflake(t,x):
    '''t is a turtle, x is the legnth of the knoch curves which combine into the snowflake'''
    koch(t,x)
    t.rt(120)
    koch(t,x)
    t.rt(120)
    koch(t,x)

    
Snowflake(bob,200)
    