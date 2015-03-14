def do_n(function, n):
    for i in range(n):
        function()

def print_something():
    print 'something'

do_n(print_something, 10)