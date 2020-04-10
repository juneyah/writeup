import sys

split_int = lambda x:map(int, x.split())

N, M = split_int(input())

matrix = [[0]*N for i in range(N)]
for x, y in map(split_int, sys.stdin):
  matrix[x-1][y-1] = 1
  matrix[y-1][x-1] = 1

def is_clique(clique, x):
  return all(matrix[x][y] for y in clique)

def max_clique(clique, x):
  m = len(clique)
  for i in range(x+1, N):
    if len(clique) + N-i < m:
      break
    if is_clique(clique, i):
      m = max(m, max_clique(clique|{i}, i))
  return m
  
print(max_clique(set(), -1))
