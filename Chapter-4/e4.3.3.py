from swampy.TurtleWorld import *

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

world = TurtleWorld()
bob = Turtle()

polygon(bob, 50, 5)