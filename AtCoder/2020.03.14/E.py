from itertools import chain, permutations, dropwhile
from heapq import merge

def listify(fn):
  def wrapper(*args, **kwargs):
    return list(fn(*args, **kwargs))
  return wrapper

def comp_wild(a,b):
  return all(x==y or "?" in (x,y) for x,y in zip(a, b))

@listify
def includers(a,b):
  for i in range(len(a)-len(b)+1):
    if comp_wild(a[i:], b):
      yield i 

@listify
def connectors(a,b):
  for i in range(max(len(a)-len(b)+1, 1), len(a)+1):
    if comp_wild(a[i:], b):
      yield i

class c_int(int):
  def __new__(cls, *args, **kwargs):
    cond = kwargs.pop("cond", lambda:True)
    i = int.__new__(cls, *args, **kwargs)
    i.cond = cond
    return i

def iter_from(it, fm):
  return dropwhile(fm.__gt__, it)

def solve(*keys):
  keys = sorted(keys, key=len, reverse=True)
  len_keys = list(map(len, keys))
  inc = { (i,j):includers(keys[i],keys[j]) for i,j in permutations(range(3), 2) }
  con = { (i,j):connectors(keys[i],keys[j]) for i,j in permutations(range(3), 2) }
  
  for i in inc[0,1]:
    for j in inc[0,2]:
      if (
        j+len_keys[2] <= i or i+len_keys[2] <= j or
        j-i in inc[1,2] or j-i in con[1,2] or i-j in con[2,1]
      ):
        return len_keys[0]
  
  def candicates(x,y,z):
    return chain(
      ( c_int(
          i+len_keys[z], 
          cond=lambda:(
            (inc[x,y] and inc[x,y][0]+len_keys[y] <= i) or 
            (inc[z,y] and len_keys[x] <= i+inc[z,y][-1]) or 
            any(
              (i-j in con[y,z] if i > j else j-i in inc[z,y])
               for j in iter_from(inc[x,y]+con[x,y], i-len_keys[y])
            )
          )
        ) for i in iter_from(con[x,z], len_keys[y]-len_keys[z]+1)
      ),
      ( c_int(
          min( i+next(iter_from(q, len_keys[x]-i+1))+len_keys[z] for i in p )
        ) for (p, q) in [sorted((con[x,y], con[y,z]), key=len)]
      ),
    )
  
  for c in merge(*( candicates(*xyz) for xyz in permutations(range(3), 3) )):
    if c.cond():
      return c
  
  return sum(len_keys)

print(solve(*(input() for i in range(3))))
