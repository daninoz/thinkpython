def is_triangle(a, b, c):
    if a > b + c or b > c + a or c > a + b:
        print 'No'
    else:
        print 'Yes'

is_triangle(5, 10, 3)