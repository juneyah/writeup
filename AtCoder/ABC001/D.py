import sys
from itertools import accumulate

def format_input(x):
  x, y = map(int, x.split("-"))
  return x//100*60+x%100, y//100*60+y%100

def format_output(x, y):
  return "{:04}-{:04}".format(x//60*100+x%60, y//60*100+y%60)

def solve():
  N = int(input())
  rain = [0]*289
  for S, E in map(format_input, sys.stdin):
    rain[S//5] += 1
    rain[(E+4)//5] -= 1

  prev = 0
  for i, c in enumerate(map(bool, accumulate(rain))):
    if c ^ prev:
      prev = c
      if c:
        s = i
      else:
        yield format_output(s*5, i*5)

print("\n".join(solve()))
