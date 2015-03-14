from swampy.TurtleWorld import *
import math

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 1000
    length = circumference / n
    polygon(t, length, n)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.0001

circle(bob, 50)

wait_for_user()