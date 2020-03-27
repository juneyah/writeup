M = 998244353
N, S = map(int, input().split())
A = map(int, input().split())
ans = 0
prev = [0]*S
for i, a in enumerate(A, 1):
  if a > S:
    continue
  prev[0] = i
  ans += prev[S-a]*(N-i+1)
  for j, s in enumerate(prev[:S-a], a):
    prev[j] += s
print(ans%M)
