# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 19:09:36 2022

@author: 44780
"""

# =============================================================================
# Write a function called draw_rect that takes a Turtle object and a Rectangle and
# uses the Turtle to draw the Rectangle. See Chapter 4 for examples using Turtle objects.
# Write a function called draw_circle that takes a Turtle and a Circle and draws the Circle.
# 
# =============================================================================
import turtle

class point:
    'a point, attributes: x,y'
class rect:
    'a rectangle, attributes: noth east and south sest most points (ne and sw)'
class circle:
    'a circle, attributes: radius and center'
pointsw=point()
pointsw.x=0
pointsw.y=0

pointne=point()
pointne.x=100
pointne.y=100

rect=rect()
rect.ne=pointne
rect.sw=pointsw

center=point()
center.x=0
center.y=0

circle=circle()
circle.radius=100
circle.center=center
a=turtle.Turtle()

def draw_rect(turtle, rect):
    "draws a rectange in a tutle instance, turtle is a turtle object and rect is a rect instance"
    turtle.goto(rect.sw.x,rect.sw.y)
    for i in range(2):
        turtle.fd(rect.ne.x-rect.sw.x)
        turtle.lt(90)
        turtle.fd(rect.ne.y-rect.sw.y)
        turtle.lt(90)
    
draw_rect(a, rect)
turtle.mainloop()

def draw_circle(turtle, circle):
    turtle.goto(circle.center.x,circle.center.y)
    turtle.rt(90)
    turtle.fd(circle.radius)
    turtle.circle(circle.radius)
    turtle.mainloop()


#draw_circle(a, circle)
