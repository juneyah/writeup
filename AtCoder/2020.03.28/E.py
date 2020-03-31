from itertools import *
from heapq import *

negint = lambda x:-int(x)

X, Y, A, B, C = map(int, input().split())
P = sorted(map(negint, input().split()))
Q = sorted(map(negint, input().split()))
R = sorted(map(negint, input().split()))

S = sum(islice(merge(islice(P, X), islice(Q, Y), R), X+Y))

print(-S)
