# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:56:22 2022

@author: 44780
"""

# =============================================================================
# Exercise 16.1. Write a function called mul_time that takes a Time object and a number and returns
# a new Time object that contains the product of the original Time and the number.
# Then use mul_time to write a function that takes a Time object that represents the finishing time
# in a race, and a number that represents the distance, and returns a Time object that represents the
# average pace (time per mile).
# =============================================================================

class Time:
    "Represents the time of day. attributes: hour, minute, second"
    
def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour,time.minute,time.second))
    
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def mul_time(time, number):
    "this function multiplies the time by a number. time is a class object"
    int_time=time_to_int(time)
    multiplied_time=int_time*number
    return int_to_time(multiplied_time)

time2=Time()
time2.hour=6
time2.minute=10
time2.second=1

print_time(mul_time(time2,2))

#speed = distance/time!

def race_pace(time, distance):
    "time is a class object and distance is a float"
    return mul_time(time,distance**-1)

print("the pace moved to cover 100 miles in 6:10:1 hours:mins:secconds (time per mile)")
print_time(race_pace(time2,100))