def do_twice(function, parameter):
    function(parameter)
    function(parameter)

def print_twice(string):
    print string
    print string

def do_four(function, parameter):
    do_twice(function, parameter)
    do_twice(function, parameter)

do_four(print_twice, 'spam')