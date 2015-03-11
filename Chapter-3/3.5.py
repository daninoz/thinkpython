def print_plus():
    print '+',

def print_dash():
    print '-',

def print_space():
    print ' ',

def print_pipe():
    print '|',


def end_line():
    print

def do_four(function):
    function()
    function()
    function()
    function()

def print_cell_horizontal_border():
    print_plus()
    do_four(print_dash)

def print_line():
    do_four(print_cell_horizontal_border)
    print_plus()
    end_line()

def print_cell_space():
    print_pipe()
    do_four(print_space)

def print_space_line():
    do_four(print_cell_space)
    print_pipe()
    end_line()

def print_horizontal_cells():
    print_line()
    do_four(print_space_line)

do_four(print_horizontal_cells)
print_line()