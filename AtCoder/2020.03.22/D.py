from collections import Counter
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
S = sum(c*(c-1)//2 for c in C.values())
for a in A:
  print(S-C[a]+1)
