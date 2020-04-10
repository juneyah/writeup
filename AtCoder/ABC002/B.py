from itertools import filterfalse

W = input()
print("".join(filterfalse("aiueo".__contains__, W)))
