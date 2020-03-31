from itertools import *
K, N = map(int, input().split())
A, B = tee(map(int, input().split()), 2)

first = next(B)
M = max(b-a for a, b in zip_longest(A, B, fillvalue=first+K))

print(K-M)
