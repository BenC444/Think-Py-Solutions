# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 10:11:58 2022

@author: 44780
"""
import math
# =============================================================================
# Write a definition for a class named Circle with attributes center and radius,
# where center is a Point object and radius is a number.

class Circle:
    "a circle in 2d space defined by its center (a point) and radius"
    
class Point:
    " a point in 2d space"
# Instantiate a Circle object that represents a circle with its center at (150, 100) and radius 75.
center1=Point()
center1.x=150
center1.y=100

Circle1=Circle()

Circle1.center=center1
Circle1.radius=75
# Write a function named point_in_circle that takes a Circle and a Point and returns True if the
# Point lies in or on the boundary of the circle.

def point_in_circle (circle,point):
    "returns true if the point lies in the boundary of the circle"
    "circle and point are their respective classes"
    if distance_between_points(point,circle.center) <circle.radius:
        return True   
    
def distance_between_points(p1,p2):
    "takes two points abd find the distance between them"
    x_diff=p1.x-p2.x
    y_diff=p1.y-p2.y
    distance = math.sqrt(x_diff**2 + y_diff**2)
    return distance

# Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True if
# the Rectangle lies entirely in or on the boundary of the circle.
class Rect:
    "this is a rectangle defined by it's two opposing points; sw and ne (south west and north east)"
    
p1=Point()
p2=Point()
p1.x=150
p1.y=100
p2.x=150
p2.y=-100

rect_eg=Rect()
rect_eg.sw=p1
rect_eg.ne=p2

def rect_in_circle(rect,circle):
    "returns True if the Rectangle lies entirely in or on the boundary of the circle."
    nw=Point()
    se=Point()
    nw.x=rect.sw.x
    nw.y=rect.ne.y
    se.x=rect.ne.x
    se.y=rect.sw.y  
    if point_in_circle(circle,rect.sw)==True and point_in_circle(circle,rect.ne)==True and point_in_circle(circle,nw)==True and point_in_circle(circle,se)==True:
        return True
    else:
        return False
print(rect_in_circle(rect_eg, Circle1)) 
#GG


# Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns
# True if any of the corners of the Rectangle fall inside the Circle. 
def rect_circle_overlap(rect,circle):
    nw=Point()
    se=Point()
    nw.x=rect.sw.x
    nw.y=rect.ne.y
    se.x=rect.ne.x
    se.y=rect.sw.y  
    if point_in_circle(circle,rect.sw)==True or point_in_circle(circle,rect.ne)==True or point_in_circle(circle,nw)==True or point_in_circle(circle,se)==True:
        return True
    else:
        return False


#Or as a more challenging version,
# return True if any part of the Rectangle falls inside the Circle

def challenge(rect,circle):
    nw=Point()
    se=Point()
    nw.x=rect.sw.x
    nw.y=rect.ne.y
    se.x=rect.ne.x
    se.y=rect.sw.y  
    if rect.ne.y>circle.center.y + circle.radius and rect.sw.y<circle.center.y - circle.radius and rect.sw.x <circle.center.y - circle.radius and rect.ne.x>circle.center.y + circle.radius:
        return False
    else:
        return True
# =============================================================================
