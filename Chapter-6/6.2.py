import math

def hypotenuse(a, b):
    a2 = a**2
    b2 = b**2
    c = math.sqrt(a2 + b2)
    return c

print hypotenuse(3, 4)