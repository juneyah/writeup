K = int(input())

total = [ [1]*10 ]

s = sum(total[-1][1:])
while s < K:
  K -= s
  total.append([sum(total[-1][max(0,i-1):i+2]) for i in range(10)])
  s = sum(total[-1][1:])

digits = []
d = 1
for subtotal in total[::-1]:
  while subtotal[d] < K:
    K -= subtotal[d]
    d += 1
  digits.append(d)
  d = max(0, d-1)

print("".join(map(str, digits)))
