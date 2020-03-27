from itertools import *
from heapq import *

def solve(H, W, grid):
  goal = (H-1, W-1)
  fixed = set()
  candicates = [(grid[0,0], (0, 0))]
  while 1:
    dist, p = heappop(candicates)
    if p == goal:
      return dist
    if p in fixed:
      continue
    fixed.add(p)
    for i in range(2):
      p1 = p[0]+i, p[1]+(1-i)
      if not (p1[0]<H and p1[1]<W) or p1 in fixed:
        continue
      x, y = p
      x1, y1 = p1
      heappush(candicates, (dist+(grid[p1] & ~grid[p]), p1))
  return None

H, W = map(int, input().split())
grid = {(i,j): int(c=="#") for i in range(H) for j, c in enumerate(input())}

print(solve(H, W, grid))
