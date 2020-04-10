m = int(input())
if m < 100:
  VV = 0
elif m <= 5000:
  VV = m // 100
elif m <= 30000:
  VV = m // 1000 + 50
elif m <= 70000:
  VV = (m // 1000 - 30)//5 + 80
else:
  VV = 89

print("{:02}".format(VV))
