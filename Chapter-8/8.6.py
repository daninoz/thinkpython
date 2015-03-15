def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

def count_letters(word, letter):
    count = 0
    start = 0
    while True:
        index = find(word, letter, start)
        if index == -1:
            return count
        else:
            count = count + 1
            start = index + 1


print count_letters('otorrinolaringologo', 'o')