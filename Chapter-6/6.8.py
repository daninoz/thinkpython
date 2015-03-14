def gcd(a, b):
    if b > a:
        temp = a
        a = b
        b = temp
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print gcd(12345, 56789)