import sys

N = int(input()) - 1
two = False
S = 0
for i in range(N+1):
  a = int(sys.stdin.read(1))
  if not two:
    two = a == 2
  if i & N == i:
    S ^= a-1

if two:
  S &= ~2

print(S)
