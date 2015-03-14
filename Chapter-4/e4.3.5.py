from swampy.TurtleWorld import *
import math

def polyline(t, n, step_length, step_angle):
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)

def square(t, length):
    polygon(t, length, 4)

def polygon(t, length, n):
    angle = 360.0 / n
    polyline(t, n, length, angle)
    

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    circumference = 2 * math.pi * r
    step_length = circumference / 1000
    n = angle * 1000 / 360
    step_angle = 360.0 / 1000
    polyline(t, n, step_length, step_angle)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0001

circle(bob, 50)
square(bob, 50)

wait_for_user()