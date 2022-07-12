# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 09:10:56 2022

@author: 44780
"""

# =============================================================================
# As an exercise, write a function called print_time that takes a Time object and prints it in
# the form hour:minute:second. Hint: the format sequence '%.2d' prints an integer using
# at least two digits, including a leading zero if necessary
# 
# =============================================================================
import copy
class Time:
    "Represents the time of day. attributes: hour, minute, second"


time = Time()
time.hour = 1
time.minute = 50
time.second = 0

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour,time.minute,time.second))

#print_time(time)    

# =============================================================================
# Write a boolean function called is_after that takes two Time objects, t1 and t2, and returns True if t1 follows t2 chronologically and False otherwise. Challenge: don’t use an
# if statement.
# =============================================================================

def is_after(t1,t2):
    if t1.hour>t2.hour:
        return True
    elif t1.minute>t2.minute:
        return True
    elif t1.second>t2.second:
        return True
    else:
        return False
    
time2=Time()
time2.hour=12
time2.minute=60
time2.second=31

#print(is_after(time, time2))

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum

def increment(time, seconds):
    time.second += seconds
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

# =============================================================================
# As an exercise, write a correct
# version of increment that doesn’t contain any loops.
# =============================================================================

def increment2(time,secconds):
    extra_mins,time.second=divmod(secconds+time.second,60)
    print("extra mins, time.secconds are:",extra_mins,time.second)
    time.hour,time.min=divmod(extra_mins+time.minute,60)

# =============================================================================
# As an exercise, write a “pure” version of increment that creates and returns a new Time
# object rather than modifying the parameter
# =============================================================================

def increment3(time,secconds):
    "this is a pure function version of increment"
    new_time=copy.copy(time)
    mins,new_time.second=divmod(secconds,60)
    print(mins, new_time.second)
    new_time.hour,new_time.min=divmod(mins,60)
    print("new time is:")
    print_time(new_time)
    
# =============================================================================
# As an exercise, rewrite
# increment using time_to_int and int_to_time
# =============================================================================

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def increment4(time,secconds):
    new_time=time_to_int(time) + secconds
    return int_to_time(new_time)