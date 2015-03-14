from swampy.TurtleWorld import *

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

world = TurtleWorld()
bob = Turtle()

square(bob, 100)

square(bob, 50)

square(bob, 25)

square(bob, 12.5)

square(bob, 6.25)