from swampy.TurtleWorld import *
import math

def polyline(t, n, step_length, step_angle):
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)

def arc(t, r, angle):
    circumference = 2 * math.pi * r
    step_length = circumference / 1000
    n = int(round(angle * 1000 / 360))
    step_angle = 360.0 / 1000
    polyline(t, n, step_length, step_angle)

def flower(t, r, thinness, n):
    angle = 360.0 / n
    for i in range(n):
        petal(t, r, thinness)
        lt(t, angle)


def petal(t, r, thinness):
    thinness = thinness / 2.0
    radio = thinness / 2 + r**2 / (8 * thinness)
    angle = math.degrees(2 * math.asin( r / (2 * radio)))
    arc(t, radio, angle)
    lt(t, 180 - angle)
    arc(t, radio, angle)
    rt(t, 180 + angle)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.000000000001

flower(bob, 200, 50, 50)

wait_for_user()