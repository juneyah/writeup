N, M = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)
selectable = sum(1 for a in A if a*4*M >= total)
if selectable >= M:
  print("Yes")
else:
  print("No")
