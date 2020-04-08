from itertools import count, product
from collections import Counter
from functools import reduce
from operator import mul

def isqrt(n):
  assert n >= 0
  if n == 0:
    return 0
  x = 1 << (n.bit_length() + 1 >> 1)
  while 1:
    x, y = (x + n // x) >> 1, x
    if x >= y:
      return y

class Qrime(object):
  def __init__(self, init=[2, 3, 5, 7]):
    self.init = init
    self.step = reduce(mul, init, 1)
    self.cand = [i for i in range(init[-1]+2, self.step+2, 2) if all(map(i.__mod__, init[1:]))]
  
  def __iter__(self):
    yield from self.init
    for i in count(0, self.step):
      for j in self.cand:
        yield i + j
Q = Qrime()

def factor(n):
  f = Counter()
  limit = isqrt(n)
  for q in Q:
    if q > limit:
      break
    while n % q ==0:
      f[q] += 1
      n //= q
    if q in f:
      limit = isqrt(n)
  if n != 1:
    f[n] += 1
  return f

def divisor(n):
  f = factor(n)
  for c in product(*map(lambda x:range(x+1), f.values())):
    yield reduce(mul, (x**y for x, y in zip(f.keys(), c) if y), 1)

N = int(input())
ans = reduce(mul, (c+1 for c in factor(N-1).values()), 1) - 1

for d in divisor(N):
  if d == 1:
    continue
  n = N
  while n % d == 0:
    n //= d
  if n % d == 1:
    ans += 1

print(ans)
