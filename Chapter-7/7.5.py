import math

def estimate_pi():
    k = 0
    summation = 0
    while True:
        first = math.factorial(4 * k)
        second = 1103 + 26390 * k
        third = math.factorial(k) ** 4
        fourth = 396 ** ( 4 * k )
        result = (first * second) / (third * fourth)
        summation = summation + result
        if result < 1e-15:
            break
        k = k + 1

    right = ((2 * math.sqrt(2)) / 9801) * summation
    pi = 1 / right
    return pi

def test_estimate_pi():
    print math.pi,
    print estimate_pi()

test_estimate_pi()