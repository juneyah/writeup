def solve(a, b, c, d):
  a, c = sorted([a, c])
  b, d = sorted([b, d])
  
  for k in range(30, 0, -1):
    block_size = 3**k
    box_size = block_size // 3
    x1, y1, x2, y2 = map(lambda x:x//box_size, (a, b, c, d))
    
    if x1 != x2 and y1 != y2:
      return c-a + d-b
    
    elif x1 == x2 and x1%3 == 1 and (y1+1)//3*3+1 < y2:
      shifted = (a+c) % (2*block_size)
      return min(shifted-2*box_size+2, 4*box_size-shifted) + d-b
    
    elif y1 == y2 and y1%3 == 1 and (x1+1)//3*3+1 < x2:
      shifted = (b+d) % (2*block_size)
      return min(shifted-2*box_size+2, 4*box_size-shifted) + c-a
  
  return c-a + d-b

for i in range(int(input())):
  print(solve(*map(lambda x:int(x)-1, input().split())))
