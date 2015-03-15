def print_transverse(string):
    index = len(string)-1
    while index >= 0:
        print string[index]
        index = index - 1

def print_transverse_alternative(string):
    index = -1
    length = len(string)
    while abs(index) <= length:
        print string[index]
        index = index - 1

print_transverse_alternative('banana')