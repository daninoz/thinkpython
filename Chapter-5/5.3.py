def check_fermat(a, b, c, n):
    if (n > 2):
        result_left = a**n + b**n
        result_right = c**n
        if (result_left == result_right):
            print 'Holy smokes, Fermat was wrong!'
        else:
            print 'Nope, that doesn\'n work'
    else:
        print 'n must be greater than 2'

def ask_user_check_fermat():
    a = int(raw_input('Enter a: '))
    b = int(raw_input('Enter b: '))
    c = int(raw_input('Enter c: '))
    n = int(raw_input('Enter n: '))
    check_fermat(a, b, c, n)

ask_user_check_fermat()