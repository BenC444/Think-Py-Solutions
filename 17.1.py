# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 12:18:07 2022

@author: 44780
"""

# =============================================================================
#  Change the attributes of Time to be a single integer representing seconds since midnight.
# Then modify the methods (and the function int_to_time) to work with the new implementation
# You should not have to modify the test code in main. When you are done, the output should
# be the same as before.
# =============================================================================

class Time:
    'a single integer which represents the number of secconds since midnight'
    def __init__(self,secs=0):
        self.secs=secs
    def int_to_time(self):
        time_int=int(self)
        allmins,secs=divmod(time_int,60)
        allhours,mins=divmod(allmins,60)
        days, hours=divmod(allhours,24)
        return ('days: %2d, %2d:%2d:%2d'%(days,hours,mins,secs))
    def __add__(self,other):
        return (self+other)
    def print_time(self):
        print(int_to_time(self))
    def increment(self,seconds):
        return self+seconds
    def is_after(self,other):
        return self>other
time=Time()
time.secs=10000

time2=Time()
time2.secs=1

#time3=time+time2

print_time(time)

# =============================================================================
# class Time:
#     """Represents the time of day."""
#     def time_to_int(self):
#         minutes = self.hour * 60 + self.minute
#         seconds = minutes * 60 + self.second
#         return seconds
#     
#     def print_time(self):
#         print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
#         
#     def increment(self, seconds):
#         seconds += self.time_to_int()
#         return int_to_time(seconds)
#     
#     def is_after(self, other):
#         return self.time_to_int() > other.time_to_int()
#     
#     def __init__(self, hour=0, minute=0, second=0):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#         
#     def __add__(self, other):
#         if isinstance(other, Time):
#             return self.add_time(other)
#         else:
#             return self.increment(other)
#         
#     def add_time(self, other):
#         seconds = self.time_to_int() + other.time_to_int()
#         return int_to_time(seconds)
#     def __radd__(self, other):
#         #this makes our add function commutitave
#         return self.__add__(other)
# =============================================================================

        