from string import ascii_lowercase as alph

def gen_pattern(N, pre="", m=0):
  if len(pre)+1 == N:
    for c in alph[:m+1]:
      yield pre+c
  else:
    for c in alph[:m]:
      yield from gen_pattern(N, pre+c, m)
    yield from gen_pattern(N, pre+alph[m], m+1)

for pattern in gen_pattern(int(input())):
  print(pattern)
