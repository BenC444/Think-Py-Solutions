# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:13:18 2022

@author: 44780
"""

start = Time()
start.hour = 9
start.minute = 45
start.second = 00

# =============================================================================
# As an exercise, rewrite time_to_int (from Section 16.4) as a method.
# =============================================================================
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

class Time:
    """Represents the time of day."""
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
        
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
        
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    def __radd__(self, other):
        #this makes our add function commutitave
        return self.__add__(other)


    
#print(start.time_to_int())
#print_time(start)
#start.print_time()
#end=start.increment(10)
#end.print_time()

#going into a method - class system gives us a different version of this:
#print(end.is_after(start))

time=Time(9,10)

time.print_time()

# =============================================================================
# As an exercise, write an init method for the Point class that takes x and y as optional
# parameters and assigns them to the corresponding attributes.
# =============================================================================
class Point:
    "X,Y co-ordinates"
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    #def print_point(self):
     #   print('(%d,%d)' % (self.x,self.y))
    def __str__(self):
        return ('(%d,%d)' %(self.x,self.y))
    def __add__(self,other):
        #this has now been modified to check if we have a point boject and work with erither a point or a tuple.
        if isinstance(other,Point):
            #returns ture if other is a Point
            sum_point=Point()
            sum_point.x=self.x+other.x
            sum_point.y=self.y+other.y
            return sum_point
        else:
            sum_point=Point()
            sum_point.x,sum_point.y=other
            
            return sum_point+self
        

point1=Point(4,5)
point2=Point(1,1)

tuple_point=(1,2)



#point.print_point()
#print(point1+point2)
# =============================================================================
# The __str__ method can be useful for debugging
# As an exercise, write a str method for the Point class. Create a Point object and print it
# =============================================================================

# =============================================================================
# As an exercise, write an add method for the Point class
# =============================================================================

# =============================================================================
# As an exercise, write an add method for Points that works with either a Point object or a
# tuple:
# =============================================================================

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c]=d[c]+1
    return d
    
print(histogram('hello boyz'))

#print(hasattr(point1,'z'))
#print (vars(time))
def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))
        
print_attributes(time)