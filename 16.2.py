# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:12:29 2022

@author: 44780
"""

# =============================================================================
# Exercise 16.2. The datetime module provides time objects that are similar to the Time objects
# in this chapter, but they provide a rich set of methods and operators. Read the documentation at
# http: // docs. python. org/ 3/ library/ datetime. html .
# 1. Use the datetime module to write a program that gets the current date and prints the day of
# the week.
# =============================================================================

import datetime

import calendar

def find_day():
    today=date.today().weekday()
    #this finds an integer which represents the days of the week ( mon-0, sun-6)
    return(calendar.day_name[today])
    
#print(find_day())

# =============================================================================
#  2. Write a program that takes a birthday as input and prints the user’s age and the number of
#  days, hours, minutes and seconds until their next birthday.
# =============================================================================
a_day = datetime.datetime(1998, 5, 25)


def time_till_birthday(birthday):
    "finds the time till your birthday, birthday should be a datetime object"
    today=datetime.datetime.now()
    difference=(today-birthday).total_seconds()
    total_mins,secconds=divmod(difference,60)
    total_hours,mins=divmod(total_mins,60)
    total_days,hours=divmod(total_hours,24)
    age,days=divmod(total_days,365)
    return ("your age is:",age,"time till birthday is:", secconds,"secconds,",mins,"mins,",hours,"hours, and ",days,"days!")
   
time_till_birthday(a_day)

 
# =============================================================================
#  3. For two people born on different days, there is a day when one is twice as old as the other.
#  That’s their Double Day. Write a program that takes two birth dates and computes their
#  Double Day.
# =============================================================================
b_day = datetime.datetime(1998, 5, 25)
 
j_day = datetime.datetime(2000, 1, 4)
 
def double_day(day1,day2):
    "day1 and 2 are date objects, day1 is older than day 2"
    age_difference=day2-day1
    result=day2+age_difference
    return result   


#print(double_day(b_day,j_day))
# =============================================================================
#  4. For a little more challenge, write the more general version that computes the day when one
#  person is n times older than the other.
# =============================================================================
def n_day(day1,day2,n):
    "day1 and 2 are date objects, day1 is older than day 2"
    "This function returns the day where the person born on day1 is n times the age of the person born on day2"
    age_difference=day2-day1
    result=day2+(n-1)*age_difference
    return result   
