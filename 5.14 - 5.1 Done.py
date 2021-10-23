# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:47:28 2021

@author: Ben Chapman
"""

"""
Write a script that reads the current time and converts it to a time of day in hours, minutes, and
seconds, plus the number of days since the epoch."""

import time


def Epochpassed():
    '''this used floor division to determine the time since 1970'''
    
    secconds_since_1970 = time.time()
    years_floor = secconds_since_1970//(365.25*24*60*60)    
    
    days_sec = secconds_since_1970 - years_floor*(365.25*24*60*60)
    days_floor = days_sec//(24*60*60)
      
    hours_sec = days_sec - days_floor*(24*60*60)
    hours_floor = hours_sec//(60*60)

    
    mins_sec = hours_sec - hours_floor*(60*60)
    mins_floor = mins_sec//60
     
    secs_s = mins_sec-mins_floor*60
    print("This is the time passed since 1st Jan 1970: \n", int(years_floor),"years\n",
          int(days_floor),"days\n", int(hours_floor),"hours\n", int(mins_floor),"mins\n", secs_s,"seconds")
    
Epochpassed()