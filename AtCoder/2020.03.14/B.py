def solve(H, W):
  if H == 1 or W == 1:
    return 1
  else:
    return (H*W+1)//2

print(solve(*map(int, input().split())))
