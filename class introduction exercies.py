# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 08:42:45 2022

@author: 44780
"""
import math
import copy
class Point:
    "Represents a point in 2D space"
    
blank=Point()
blank.x=3
blank.y=4

origin=Point()
origin.x=0
origin.y=0

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))
    
def distance_between_points(p1,p2):
    "takes two points abd find the distance between them"
    x_diff=p1.x-p2.x
    y_diff=p1.y-p2.y
    distance = math.sqrt(x_diff**2 + y_diff**2)
    print(distance)

#distance_between_points(blank,origin)

class Rectangle:
    "represents a rectange in 2D space"

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(rect):
    "Rect is a class object representing a rectangle"
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def grow_rectangle(rect, dwidth, dheight):
    "Rect is a class object representing a rectangle, dwitdth and dheight are the ammount you want to grow height and width respectively"
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect,dx,dy):
    "dx and dy are directions in which rect is moved"
    rect.corner.x+=dx
    rect.corner.y+=dy
    return rect

#As an exercise, write a version of move_rectangle that creates and returns a new Rectangle
#instead of modifying the old one.

def move_rectangleV2(rect,dx,dy):
    "rect is a class, dx and dy are the distance the reect is moved"
    rect2=copy.deepcopy(rect)
    rect2=move_rectangle(rect2,dx,dy)
    return rect2

print(move_rectangleV2(box, 2, 1 )==move_rectangle(box, 2, 1))
print(print_point(move_rectangleV2(box, 2, 1 ).corner), print_point(move_rectangle(box, 2, 1).corner))